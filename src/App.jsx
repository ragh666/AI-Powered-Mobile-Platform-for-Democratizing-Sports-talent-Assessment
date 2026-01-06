import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

import Dashboard from "./components/Dashboard";
import SprintTest from "./pages/SprintTest";
import AthleteProfile from "./components/AthleteProfile";
import CalendarPage from "./components/CalendarPage";
import Prediction from "./components/Prediction";
import History from "./components/History";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/sprint-test" element={<SprintTest />} />
        <Route path="/profile" element={<AthleteProfile />} />
        <Route path="/calendar" element={<CalendarPage />} />
        <Route path="/prediction" element={<Prediction />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

