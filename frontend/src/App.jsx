import './App.css'
import { useState } from 'react'
import { generateResult } from './api'

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

    const result = await generateResult(input)
    setSentiment(result.sentiment)
    setLoading(false)
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

      <footer className="footer">
        <p>
          This app uses AI models to guess the sentiment of a user's text entries. It is not always one hundred percent
          accurate. Do not plan to use this dashboard for serious decisions; we built this for AI demonstration.
        </p>
        <p>Powered by AI Sentiment Engine</p>
      </footer>
    </div>
  )
}

export default App
