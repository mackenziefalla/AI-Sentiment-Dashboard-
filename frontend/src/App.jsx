import "./App.css";
import { useState } from "react";
import { analyzeText } from "./api";

const emojiMap = {
  Positive: "😊",
  Neutral: "😐",
  Negative: "☹️",
};

function App() {
  const [input, setInput] = useState("");
  const [data, setData] = useState({}); // now handles multiple aspect results
  const [loading, setLoading] = useState(false);

  const diagnoseSentence = async () => {
    // if the input is empty, don't call the api
    if (!input.trim()) {
      alert("Please enter a sentence first!");
      return;
    }

    setLoading(true);
    setData({});

    try {
      // retrieve sentiment analysis from api call
      const data = await analyzeText(input);
      setData(data || {});
    } catch (error) {
      console.error("Error analyzing:", error);
      setData({ overall: { sentiment: "Error", score: "N/A" } });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">AI Sentiment Dashboard</h1>

      <p className="subtitle">
        The AI Sentiment Dashboard analyzes what people feel — and which parts
        of a message express positive, neutral, or negative emotions.
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
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </div>

      {Object.keys(data).length > 0 && data.overall && (
        <div className="result-card">
          <h2>Results</h2>
          <div>
            <strong>Overall Sentiment</strong> →{" "}
            {emojiMap[data.overall.sentiment] || ""} {data.overall.sentiment} (
            {data.overall.score * 100}%)
          </div>
          {data.results &&
            data.results.map((r, i) => (
              <div key={i} className="result-line">
                <strong>{r.aspect}</strong> → {emojiMap[r.sentiment] || ""}{" "}
                {r.sentiment} ({r.score * 100}%)
              </div>
            ))}
        </div>
      )}

      <footer className="footer">
        <p>
          This app uses AI models to detect emotional tone and context. Results
          are probabilistic, not deterministic.
        </p>
        <p>Built for FAU CAP 4630 – Responsible AI Project</p>
      </footer>
    </div>
  );
}

export default App;
