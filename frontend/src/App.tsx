import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Checking backend...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((response) => response.json())
      .then((data) => {
        setStatus(data.status);
      })
      .catch(() => {
        setStatus("Backend unavailable");
      });
  }, []);

  return (
    <div>
      <h1>Enterprise Knowledge Assistant</h1>

      <p>
        Backend status: {status}
      </p>
    </div>
  );
}

export default App;