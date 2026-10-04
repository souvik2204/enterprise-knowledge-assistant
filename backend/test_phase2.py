from app.db.database import SessionLocal
from app.models import (
    User,
    Document,
    DocumentChunk,
    DocumentPermission,
    Job,
    AuditLog,
)


db = SessionLocal()

try:
    user = User(
        email="developer@example.com",
        name="Developer",
        role="cloud_engineer",
    )

    db.add(user)
    db.flush()

    document = Document(
        title="OpenShift Administration Guide",
        content="This document contains OpenShift administration information.",
        source="openshift-guide.txt",
        department="Cloud Engineering",
        classification="internal",
        owner=user,
    )

    db.add(document)
    db.flush()

    permission = DocumentPermission(
        document_id=document.id,
        role="cloud_engineer",
        access_type="read",
    )

    db.add(permission)

    chunk = DocumentChunk(
        document_id=document.id,
        chunk_index=0,
        content="OpenShift administrators manage clusters and workloads.",
        metadata_={
            "section": "Administration",
            "page": 1,
        },
    )

    db.add(chunk)

    job = Job(
        job_type="document_ingestion",
        status="completed",
        document_id=document.id,
        attempts=1,
    )

    db.add(job)

    audit_log = AuditLog(
        user_id=user.id,
        action="DOCUMENT_UPLOAD",
        resource_type="document",
        resource_id=document.id,
        metadata_={
            "source": "openshift-guide.txt",
        },
    )

    db.add(audit_log)

    db.commit()

    print("User ID:", user.id)
    print("Document ID:", document.id)
    print("Chunk ID:", chunk.id)
    print("Permission ID:", permission.id)
    print("Job ID:", job.id)
    print("Audit Log ID:", audit_log.id)

    print("\nDocument owner:", document.owner.name)
    print("Chunks:", len(document.chunks))
    print("Permissions:", len(document.permissions))

except Exception:
    db.rollback()
    raise

finally:
    db.close()