function ResultCard({ speed }) {
  return (
    <div className="card">
      <h2>AI Result</h2>
      <p>Average Speed: <b>{speed} m/s</b></p>
      <p>Performance Level: <b>Excellent</b></p>
    </div>
  );
}

export default ResultCard;
