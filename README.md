# 🧠 Math Solver AI: Full-Stack Calculator

This is a **full-stack application** designed to solve complex math problems step-by-step using a powerful **Large Language Model (LLM)**.  
It features a **Python (Flask)** backend to handle secure API calls and a **React** frontend for an interactive user experience.

---

## ✨ Key Technologies

**Backend:** Python 3, Flask, Flask-CORS  
**Frontend:** React, Node.js  
**AI Model:** Google Gemini 2.5 Flash  
**API Integration:** OpenAI Python SDK (configured for the Gemini API)

---

## 📁 Project Structure

A typical project structure looks like this:

math-solver/
├── backend/
│ ├── app.py # Flask application and API endpoint
│ ├── requirements.txt
│ └── .env # For storing your API Key securely
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── ... (other React files)
└── README.md


---
## 🛠️ Setup and Installation

Follow the steps below to set up both the **backend (Flask/Python)** and **frontend (React/Node.js)** environments for the Math Solver AI project.

---

### 1. 🔑 API Key Setup (Critical)

Your **Gemini API key** must remain **confidential**.  
This project uses a `.env` file and the `python-dotenv` package to securely load environment variables.

#### Steps:

1. **Get Your Key**  
   Obtain a Gemini API Key from [Google AI Studio](https://makersuite.google.com/app/apikey).

2. **Create `.env` File**  
   Inside your `backend/` directory, create a new file named `.env`.

3. **Add Your API Key**  
   Paste the following line into the `.env` file (replace with your actual key):

   ```bash
   GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"

### 2. 💻 Frontend Setup (React + TypeScript)

The **frontend** is built using **React** with **TypeScript** for type safety and maintainability.  
It provides the user interface for submitting math problems and displaying the step-by-step solutions from the Flask backend.

---

#### 🧩 1. Create the React App (if not already created)

If the `frontend/` directory doesn’t exist yet, create a new React project using the official TypeScript template:

```bash
npx create-react-app frontend --template typescript
