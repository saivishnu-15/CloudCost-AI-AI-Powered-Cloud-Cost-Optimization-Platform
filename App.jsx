import Dashboard from "./components/Dashboard";

export default function App() {
  return (
    <div
      style={{
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "20px",
      }}
    >
      <h1
        style={{
          fontSize: "32px",
          marginBottom: "20px",
        }}
      >
        Cloud Cost Optimizer AI 🚀
      </h1>

      <Dashboard />
    </div>
  );
}
