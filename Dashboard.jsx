import { useEffect, useState } from "react";
import { getResources, getWaste } from "../api";

export default function Dashboard() {
  const [resources, setResources] = useState([]);
  const [waste, setWaste] = useState([]);

  useEffect(() => {
    getResources().then((res) => setResources(res.data));
    getWaste().then((res) => setWaste(res.data));
  }, []);

  return (
    <div style={{ display: "flex", gap: "20px" }}>
      <div
        style={{
          flex: 1,
          background: "#1e293b",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
        <h2>Cloud Resources</h2>

        {resources.map((r) => (
          <div
            key={r.id}
            style={{
              background: "#334155",
              padding: "10px",
              marginBottom: "10px",
              borderRadius: "8px",
            }}
          >
            <h3>{r.name}</h3>
            <p>Type: {r.type}</p>
            <p>CPU: {r.cpu_utilization}%</p>
            <p>Cost: ${r.cost_per_month}</p>
          </div>
        ))}
      </div>

      <div
        style={{
          flex: 1,
          background: "#1e293b",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
        <h2>AI Optimization Insights</h2>

        {waste.map((w, i) => (
          <div
            key={i}
            style={{
              background: "#7f1d1d",
              padding: "10px",
              marginBottom: "10px",
              borderRadius: "8px",
            }}
          >
            <h3>{w.name}</h3>
            <p>Issue: {w.issue}</p>
            <p>Suggestion: {w.suggestion}</p>
            <p>Savings: ${w.savings}</p>
            <p>{w.ai}</p>
          </div>
        ))}
      </div>
    </div>
  );
}