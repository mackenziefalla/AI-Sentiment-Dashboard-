import './App.css'
import { useState } from 'react'

function App() {

    const [input, setInput] = useState("")
    const diagnoseSentence = () => {
        console.log("Diagnosing sentiment: " + input)
    }
    return (
        <>
            <h1>AI Sentiment Dashboard</h1>
            <p>{"Subject to change -> The AI Sentiment Dashboard will take any sentence as an input, and predict the sentiment behind it. Were you happy, sad, angry, who knows? The AI Sentiment Dashboard does. Probably."}</p>
            <div>
                <input type='text' placeholder='How are you feeling?' onChange={(e) => setInput(e.target.value)} />
                <button onClick={ diagnoseSentence }>Diagnose</button>
            </div>
        </>
    )
}

export default App
