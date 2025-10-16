import "./App.css";
import { useState } from "react";
import { analyzeText } from "./api"; // ✅ correct import


const emojiMap = {
  Positive: "😊",
  Neutral: "😐",
  Negative: "☹️",
};

function App() {
  const [input, setInput] = useState("");
  const [results, setResults] = useState([]); // now handles multiple aspect results
  const [loading, setLoading] = useState(false);

  const diagnoseSentence = async () => {
    if (!input.trim()) {
      alert("Please enter a sentence first!");
      return;
    }

    setLoading(true);
    setResults([]);

    try {
      // ✅ use new backend call
      const data = await analyzeText(input);
      setResults(data.results || []);
    } catch (error) {
      console.error("Error analyzing:", error);
      setResults([{ aspect: "Error", sentiment: "N/A", score: 0 }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">AI Sentiment Dashboard</h1>

      <p className="subtitle">
        The AI Sentiment Dashboard analyzes what people feel — and which parts of a message express
        positive, neutral, or negative emotions.
      </p>

      <div className="input-section">
        <input
          type="text"
          placeholder='Try: "The professor was great but the homework was awful."'
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="sentiment-input"
        />
        <button onClick={diagnoseSentence} className="diagnose-btn" disabled={loading}>
        </button>
      </div>

      {results.length > 0 && (
  <div className="result-card">
    <h2>Results</h2>
    {results.map((r, i) => (
      <div key={i} className="result-line">
        <strong>{r.aspect}</strong> → {emojiMap[r.sentiment] || ""} {r.sentiment} ({r.score}%)
      </div>
    ))}
  </div>
)}



      <footer className="footer">
        <p>
          This app uses AI models to detect emotional tone and context. Results are probabilistic,
          not deterministic.
        </p>
        <p>Built for FAU CAP 4630 – Responsible AI Project</p>
      </footer>
    </div>
  );
}

export default App;
