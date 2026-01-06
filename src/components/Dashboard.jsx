import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import {
  FaRunning,
  FaRobot,
  FaUser,
  FaHistory,
  FaCalendarAlt,
} from "react-icons/fa";

function IconCard({ icon, title, path }) {
  const navigate = useNavigate();

  return (
    <motion.div
      className="icon-card"
      whileHover={{ scale: 1.08 }}
      whileTap={{ scale: 0.95 }}
      onClick={() => navigate(path)}
    >
      <div className="icon">{icon}</div>
      <p>{title}</p>
    </motion.div>
  );
}

function Dashboard() {
  return (
    <motion.div
      className="page"
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
    >
      {/* CENTER CONTENT */}
      <div className="center-container">
        <h2 className="welcome-title">Welcome Athlete 👋</h2>
        <p className="welcome-subtitle">
          Measure sprint speed, analyze performance using AI,
          and track your athletic growth.
        </p>

        {/* ICON GRID */}
        <div className="icon-grid">
          <IconCard
            icon={<FaRunning />}
            title="Sprint Test"
            path="/sprint-test"
          />
          <IconCard
            icon={<FaRobot />}
            title="AI Prediction"
            path="/prediction"
          />
          <IconCard
            icon={<FaUser />}
            title="Profile"
            path="/profile"
          />
          <IconCard
            icon={<FaHistory />}
            title="History"
            path="/history"
          />
          <IconCard
            icon={<FaCalendarAlt />}
            title="Calendar"
            path="/calendar"
          />
        </div>
      </div>
    </motion.div>
  );
}

export default Dashboard;
