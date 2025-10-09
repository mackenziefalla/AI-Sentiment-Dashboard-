export async function generateResult(prompt) {
  const result = await fetch("http://127.0.0.1:8000/api/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });

  if (!result.ok) {
    console.error("Backend error:", result.status, await result.text());
    throw new Error("Error analyzing text");
  }

  const data = await result.json();
  return data;
}
