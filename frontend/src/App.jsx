import { use, useEffect, useState } from "react";

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

  useEffect(() => {
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

    fetchData();
  }, []);

  return (
    <>
      <h1>Hello, Maincode!</h1>
      <p className="read-the-docs">
        Click on the button to get get data from the API.
      </p>
      <p>API Status: {message}</p>
      <button onClick={() => window.location.reload()}>Retry API Call</button>
    </>
  );
}

export default App;
