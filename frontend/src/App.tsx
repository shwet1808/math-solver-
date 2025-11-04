import React, { useState } from "react";
import axios, { AxiosError } from "axios";
import "./App.css";

// Define API response types
interface AskRequest {
  question: string;
}

interface AskSuccessResponse {
  response: string;
}

interface AskErrorResponse {
  error: string;
}

function App() {
  const [question, setQuestion] = useState<string>("");
  const [response, setResponse] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!question.trim()) {
      setError("Please enter a math question.");
      return;
    }

    setLoading(true);
    setResponse("");
    setError("");

    try {
      const requestData: AskRequest = { question };
      const res = await axios.post<AskSuccessResponse>(
        "http://localhost:5000/api/ask",
        requestData,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      setResponse(res.data.response);
    } catch (err) {
      if (axios.isAxiosError(err)) {
        const error = err as AxiosError<AskErrorResponse>;
        console.error("API Error:", error);

        if (error.response) {
          // Backend returned an error (4xx, 5xx)
          setError(error.response.data.error || "Server returned an error.");
        } else if (error.request) {
          // No response (e.g., backend not running)
          setError("Failed to connect to the AI backend. Is it running?");
        } else {
          setError("An unexpected error occurred.");
        }
      } else {
        setError("An unexpected error occurred.");
        console.error("Non-Axios Error:", err);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🧠 Math Tutor AI</h1>
        <p>Ask any math question — get step-by-step answers!</p>
      </header>

      <main className="App-main">
        <form onSubmit={handleSubmit}>
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="e.g., How many 4-letter words can be formed from 'MATH' without repetition?"
            rows={4}
            aria-label="Enter your math question"
            disabled={loading}
          />
          <button type="submit" disabled={loading}>
            {loading ? "Thinking..." : "Get Step-by-Step Answer"}
          </button>
        </form>

        {error && <div className="error-message">{error}</div>}
        {response && <div className="ai-response">{response}</div>}
      </main>
    </div>
  );
}

export default App;
