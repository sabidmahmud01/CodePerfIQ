import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000/api/analyze";

const sampleCode = `def find_duplicates(numbers):
    duplicates = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])

    return duplicates`;

function App() {
  const [code, setCode] = useState(sampleCode);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function analyzeCode() {
    setLoading(true);
    setError("");
    setAnalysis(null);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ code }),
      });

      if (!response.ok) {
        throw new Error("Failed to analyze code.");
      }

      const data = await response.json();
      setAnalysis(data);
    } catch (err) {
      setError("Could not connect to the backend. Make sure FastAPI is running.");
    } finally {
      setLoading(false);
    }
  }

  function clearCode() {
    setCode("");
    setAnalysis(null);
    setError("");
  }

  function loadSample() {
    setCode(sampleCode);
    setAnalysis(null);
    setError("");
  }

  return (
    <div className="app">
      <header className="hero">
        <div>
          <p className="eyebrow">AI Code Performance Analyzer</p>
          <h1>CodePerfIQ</h1>
          <p className="heroText">
            Paste code, detect performance bottlenecks, estimate complexity, and get
            an AI-generated explanation.
          </p>
        </div>

        <div className="statusCard">
          <span className="statusDot"></span>
          <p>FastAPI + Gemini AI</p>
        </div>
      </header>

      <main className="layout">
        <section className="panel editorPanel">
          <div className="panelHeader">
            <div>
              <h2>Input Code</h2>
              <p>Paste Python code below and run the analyzer.</p>
            </div>

            <div className="buttonGroup">
              <button className="secondaryButton" onClick={loadSample}>
                Load Sample
              </button>
              <button className="secondaryButton" onClick={clearCode}>
                Clear
              </button>
            </div>
          </div>

          <textarea
            value={code}
            onChange={(event) => setCode(event.target.value)}
            placeholder="Paste your code here..."
            spellCheck="false"
          />

          <button className="primaryButton" onClick={analyzeCode} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze Code"}
          </button>

          {error && <p className="error">{error}</p>}
        </section>

        <section className="panel resultPanel">
          <div className="panelHeader">
            <div>
              <h2>Analysis Result</h2>
              <p>Rule-based findings plus AI explanation.</p>
            </div>
          </div>

          {!analysis && !loading && (
            <div className="emptyState">
              <h3>No analysis yet</h3>
              <p>Click Analyze Code to see results here.</p>
            </div>
          )}

          {loading && (
            <div className="emptyState">
              <h3>Analyzing...</h3>
              <p>CodePerfIQ is checking your code and preparing an AI explanation.</p>
            </div>
          )}

          {analysis && (
            <div className="results">
              <div className="resultGrid">
                <div className="metricCard">
                  <p>Language</p>
                  <h3>{analysis.language}</h3>
                </div>

                <div className="metricCard">
                  <p>Complexity</p>
                  <h3>{analysis.complexity}</h3>
                </div>
              </div>

              <div className="resultBlock">
                <h3>Summary</h3>
                <p>{analysis.summary}</p>
              </div>

              <div className="resultBlock">
                <h3>Bottlenecks</h3>
                {analysis.bottlenecks?.length > 0 ? (
                  <ul>
                    {analysis.bottlenecks.map((item, index) => (
                      <li key={index}>{item}</li>
                    ))}
                  </ul>
                ) : (
                  <p>No major bottlenecks detected.</p>
                )}
              </div>

              <div className="resultBlock">
                <h3>Suggestions</h3>
                {analysis.suggestions?.length > 0 ? (
                  <ul>
                    {analysis.suggestions.map((item, index) => (
                      <li key={index}>{item}</li>
                    ))}
                  </ul>
                ) : (
                  <p>No suggestions available.</p>
                )}
              </div>

              <div className="aiBlock">
                <h3>AI Explanation</h3>
                <p>{analysis.ai_explanation}</p>
              </div>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;