import { useState } from "react";

function SprintTest() {
  const [speed, setSpeed] = useState(null);

  const runTest = () => {
    // mock result (you can connect AI later)
    const result = (Math.random() * 10 + 20).toFixed(2);
    setSpeed(result);
  };

  return (
    <div className="page">
      <div className="card">
        <h2>Sprint Speed Test</h2>
        <p>Click below to simulate sprint analysis</p>

        <button onClick={runTest}>Start Sprint Test</button>

        {speed && (
          <div className="result-box">
            <h3>Result</h3>
            <p>Speed: <strong>{speed} km/h</strong></p>
          </div>
        )}
      </div>
    </div>
  );
}

export default SprintTest;
