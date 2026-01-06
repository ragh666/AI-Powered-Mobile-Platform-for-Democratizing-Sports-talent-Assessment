import { useEffect, useState } from "react";

function History() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const data =
      JSON.parse(localStorage.getItem("sprintHistory")) || [];
    setHistory(data);
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Performance History</h2>

      {history.length === 0 ? (
        <p>No records yet</p>
      ) : (
        <ul>
          {history.map((item, index) => (
            <li key={index}>
              ⏱ {item.time}s | ⭐ {item.rating} | 📅 {item.date}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default History;
