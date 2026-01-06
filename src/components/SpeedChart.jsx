import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const data = [
  { run: 1, speed: 6.2 },
  { run: 2, speed: 6.8 },
  { run: 3, speed: 7.1 },
  { run: 4, speed: 7.4 }
];

function SpeedChart() {
  return (
    <>
      <h2>Sprint Speed Progress</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <XAxis dataKey="run" />
          <YAxis />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="speed"
            stroke="#00e5ff"
            strokeWidth={3}
          />
        </LineChart>
      </ResponsiveContainer>
    </>
  );
}

export default SpeedChart;
