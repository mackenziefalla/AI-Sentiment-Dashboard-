export async function generateResult(prompt) {

    //TODO: change "localhost:5000" to the host url
    //If testing locally, cd into backend, and run 'uvicorn app:app --reload --port 5000'
    //make sure to 'pip install fastapi uvicorn'
    //This will run a locally hosted server that the app can call an api to
    const result = await fetch("http://localhost:5000/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
    });

    const data = await result.json()
    return data
}