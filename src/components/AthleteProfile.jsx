import { useState, useEffect } from "react";

function AthleteProfile() {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem("athleteProfile"));
    if (data) {
      setName(data.name);
      setAge(data.age);
    }
  }, []);

  const saveProfile = () => {
    localStorage.setItem(
      "athleteProfile",
      JSON.stringify({ name, age })
    );
    alert("Profile saved");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Athlete Profile</h2>

      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <br /><br />
      <input
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />
      <br /><br />
      <button onClick={saveProfile}>Save</button>
    </div>
  );
}

export default AthleteProfile;
