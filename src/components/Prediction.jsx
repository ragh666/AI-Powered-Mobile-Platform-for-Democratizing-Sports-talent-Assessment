function Prediction() {
  const history =
    JSON.parse(localStorage.getItem("sprintHistory")) || [];

  if (history.length < 3) {
    return (
      <div style={{ padding: "20px" }}>
        <h2>AI Sprint Prediction</h2>
        <p>Add at least 3 sprint records to see prediction.</p>
      </div>
    );
  }

  const times = history.map(h => Number(h.time));
  const avg =
    times.reduce((sum, t) => sum + t, 0) / times.length;

  const last = times[times.length - 1];
  const prev = times[times.length - 2];

  const trend =
    last < prev ? "Improving 📈" : "Declining 📉";

  const predicted = (avg - 0.15).toFixed(2);

  let level = "Beginner";
  if (predicted < 11) level = "Pro";
  else if (predicted < 14) level = "Intermediate";

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Sprint Prediction</h2>
      <p>Average Time: {avg.toFixed(2)} s</p>
      <p>Last Sprint: {last} s</p>
      <p>Trend: {trend}</p>
      <h3>Predicted Next Sprint: {predicted} s</h3>
      <h3>Predicted Level: {level}</h3>
    </div>
  );
}

export default Prediction;
