import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  useEffect(() => {
    fetch("/api/hello")
      .then((res) => res.json())
      .then((data) => {
        setMessage(data.message);
      });
  }, []);

  return (
    <div className="flex items-center justify-center h-screen">
      <h1 className="font-bold">{message}</h1>
    </div>
  );
}

export default App;
