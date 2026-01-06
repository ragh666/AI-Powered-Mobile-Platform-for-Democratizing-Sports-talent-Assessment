function Prediction() {
  const history =
    JSON.parse(localStorage.getItem("sprintHistory")) || [];

  if (history.length < 2) {
    return <p>Not enough data for prediction</p>;
  }

  const times = history.map(h => Number(h.time));
  const avg =
    times.reduce((a, b) => a + b, 0) / times.length;

  const last = times[times.length - 1];

  const trend =
    last < avg ? "Improving 📈" : "Needs Improvement 📉";

  const predicted = (avg - 0.2).toFixed(2);

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Performance Prediction</h2>
      <p>Average Time: {avg.toFixed(2)}s</p>
      <p>Last Sprint: {last}s</p>
      <p>Trend: {trend}</p>
      <p>Predicted Next Sprint: {predicted}s</p>
    </div>
  );
}

export default Prediction;
