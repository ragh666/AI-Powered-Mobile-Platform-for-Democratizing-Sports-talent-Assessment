function ScoreBadge({ score }) {
  return (
    <div className="score-badge">
      <h3>AI Score</h3>
      <span>{score}</span>
    </div>
  );
}

export default ScoreBadge;
