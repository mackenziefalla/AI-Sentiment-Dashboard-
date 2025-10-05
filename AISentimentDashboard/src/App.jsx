import './App.css'
import { useState } from 'react'

function App() {
  const [input, setInput] = useState("")
  const [sentiment, setSentiment] = useState(null)
  const [loading, setLoading] = useState(false)

  const diagnoseSentence = async () => {
    if (!input.trim()) {
      alert("Please enter a sentence first!")
      return
    }

    setLoading(true)
    setSentiment(null)

    // Simulate AI prediction (replace with actual fetch() later)
    setTimeout(() => {
      const moods = ["😊 Positive", "😐 Neutral", "😞 Negative", "😡 Angry", "😢 Sad"]
      const randomMood = moods[Math.floor(Math.random() * moods.length)]
      setSentiment(randomMood)
      setLoading(false)
    }, 1500)
  }

  return (
    <div className="app-container">
      <h1 className="title">AI Sentiment Dashboard</h1>

      <p className="subtitle">
        The AI Sentiment Dashboard analyzes how you feel — whether you're happy, sad, or somewhere in between.
      </p>

      <div className="input-section">
        <input
          type="text"
          placeholder="Type how you're feeling..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="sentiment-input"
        />
        <button onClick={diagnoseSentence} className="diagnose-btn" disabled={loading}>
          {loading ? "Analyzing..." : "Diagnose"}
        </button>
      </div>

      {sentiment && (
        <div className="result-card">
          <h2>Result</h2>
          <p className="sentiment-text">{sentiment}</p>
        </div>
      )}

      <footer className="footer"> Powered by AI Sentiment Engine</footer>
    </div>
  )
}

export default App

