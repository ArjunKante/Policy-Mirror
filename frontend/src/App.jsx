import { useState } from "react";

function App() {
  const [age, setAge] = useState("");
  const [income, setIncome] = useState("");
  const [state, setState] = useState("");
  const [status, setStatus] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // ✅ API base URL from environment (Vercel / local)
  const API_BASE = import.meta.env.VITE_API_BASE_URL;

  async function analyzePolicy() {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch(`${API_BASE}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          policy: "union_budget_2024",
          user_profile: {
            age: Number(age),
            income: Number(income),
            state,
            status,
          },
        }),
      });

      if (!response.ok) {
        throw new Error("Backend error");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Could not connect to backend");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto", fontFamily: "Arial" }}>
      <h1>🪞 PolicyMirror</h1>
      <p>See how government policies affect you personally.</p>

      <input
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />
      <br /><br />

      <input
        placeholder="Annual Income (₹)"
        value={income}
        onChange={(e) => setIncome(e.target.value)}
      />
      <br /><br />

      <input
        placeholder="State"
        value={state}
        onChange={(e) => setState(e.target.value)}
      />
      <br /><br />

      <input
        placeholder="Status (student / working / senior)"
        value={status}
        onChange={(e) => setStatus(e.target.value)}
      />
      <br /><br />

      <button onClick={analyzePolicy}>
        Analyze Policy
      </button>

      {loading && <p>Analyzing policy...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Personal Impact</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </d
