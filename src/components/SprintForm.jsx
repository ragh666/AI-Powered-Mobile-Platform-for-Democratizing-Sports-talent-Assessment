import { useState } from "react";

function SprintForm() {
  const [time, setTime] = useState("");

  const getRating = (time) => {
    if (time < 11) return "Pro";
    if (time < 14) return "Intermediate";
    return "Beginner";
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const rating = getRating(time);

    const newResult = {
      time,
      rating,
      date: new Date().toLocaleDateString(),
    };

    const existing =
      JSON.parse(localStorage.getItem("sprintHistory")) || [];

    localStorage.setItem(
      "sprintHistory",
      JSON.stringify([...existing, newResult])
    );

    setTime("");
    alert("Result saved!");
  };

  return (
    
    <div style={{ padding: "20px" }}>
      <h2>Sprint Speed Test</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="number"
          step="0.01"
          placeholder="Sprint time (seconds)"
          value={time}
          onChange={(e) => setTime(e.target.value)}
          required
        />
        <br /><br />
        <button type="submit">Save Result</button>
      </form>
    </div>
  );
}

export default SprintForm;
