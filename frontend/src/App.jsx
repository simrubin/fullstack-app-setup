import { useEffect, useState } from "react";
import Silk from "./components/Backgrounds/Silk/Silk.jsx";

import "./App.css";

const tryCatch = async (func) => {
  try {
    return [await func(), null];
  } catch (error) {
    return [null, error];
  }
};

function App() {
  const [message, setMessage] = useState("Loading...");

  const fetchData = async () => {
    const [data, error] = await tryCatch(async () => {
      const res = await fetch("/api/healthcheck");
      return await res.json();
    });

    if (error) {
      console.error("Error fetching data:", error);
      setMessage("Error connecting to API");
    } else {
      console.log("API Response:", data); // Debug log
      // The API returns {status: "OK"}, not {message: "..."}
      setMessage(data.status || JSON.stringify(data));
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
          color="#007c11ff"
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
        <h1 style={{ color: "white" }}>Hello, Maincode!</h1>
        <p style={{ color: "white" }} className="read-the-docs">
          Click on the button to check the status of the API.
        </p>
        <button onClick={fetchData}>Retry API Call</button>
        <p style={{ color: "white" }}>API Status: {message}</p>
      </div>
    </>
  );
}

export default App;
