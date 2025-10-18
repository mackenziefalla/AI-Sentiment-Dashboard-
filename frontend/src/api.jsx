export async function analyzeText(text) {
  const response = await fetch("http://127.0.0.1:8000/api/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  if (!response.ok) {
    console.error("Backend error:", response.status, await response.text());
    throw new Error("Error analyzing text");
    }

    const data = await response.json();
  console.log(data)
  return data;
}
