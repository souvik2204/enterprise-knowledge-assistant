
from app.db.database import SessionLocal
from app.models import User, Document, DocumentChunk

db = SessionLocal()

try:
    user = User(
        email="test@example.com",
        name="Test User",
        role="user",
    )

    db.add(user)
    db.flush()

    document = Document(
        title="Cloud Deployment Guide",
        content="This guide explains cloud deployment.",
        source="cloud_guide.txt",
        department="Cloud Engineering",
        classification="internal",
        owner=user,
    )

    db.add(document)
    db.flush()

    chunk = DocumentChunk(
        document_id=document.id,
        chunk_index=0,
        content="This section explains deployment prerequisites.",
        metadata_={"section": "Prerequisites"},
    )

    db.add(chunk)
    db.commit()

    print("User ID:", user.id)
    print("Document ID:", document.id)
    print("Chunk ID:", chunk.id)
    print("Document owner:", document.owner.name)
    print("Number of chunks:", len(document.chunks))

except Exception:
    db.rollback()
    raise

finally:
    db.close()