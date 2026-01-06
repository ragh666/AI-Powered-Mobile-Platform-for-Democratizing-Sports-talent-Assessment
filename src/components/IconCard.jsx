function IconCard({ icon, title, path }) {
  const navigate = useNavigate();

  return (
    <div className="icon-card" onClick={() => navigate(path)}>
      <div className="icon-circle">{icon}</div>
      <h3>{title}</h3>
    </div>
  );
}
