import { useEffect, useState } from "react";
import Silk from "./components/Backgrounds/Silk/Silk.jsx";

import "./App.css";

function App() {
  const [message, setMessage] = useState("Loading...");

  const fetchData = async () => {
    try {
      const apiUrl = import.meta.env.VITE_API_URL;
      const endpoint = `${apiUrl}/api/healthcheck`;
      console.log("Fetching from:", endpoint); // Debug log
      const res = await fetch(endpoint);
      const data = await res.json();
      console.log("API Response:", data); // Debug log
      setMessage(data.status || JSON.stringify(data));
    } catch (error) {
      console.error("Error fetching data:", error);
      setMessage("Error connecting to API");
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      <div
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          width: "100vw",
          height: "100vh",
          zIndex: -1,
        }}
      >
        <Silk
          speed={3}
          scale={1}
          color="#02540dff"
          noiseIntensity={1.2}
          rotation={0.2}
        />
      </div>

      <div
        style={{
          position: "relative",
          zIndex: 1,
          padding: "20px",
          textAlign: "center",
        }}
      >
        <h1 style={{ color: "white" }}>Hello, World!</h1>
        <p style={{ color: "white" }} className="read-the-docs">
          Click on the button to check the status of the API.
        </p>
        <button onClick={fetchData}>Call API</button>
        <p style={{ color: "white", fontWeight: "bold" }}>
          API Status: {message}
        </p>
      </div>
    </>
  );
}

export default App;
