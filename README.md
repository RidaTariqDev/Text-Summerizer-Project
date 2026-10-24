# Text-Summerizer-Project

## About the Project
AI Text Summarizer is a simple Python web application that uses Google's Gemini API to summarize text into three concise bullet points.

This project was developed as part of an internship task on AI APIs and Application Development.

## Features
- Summarizes text using Google's Gemini AI.
- Simple and user-friendly web interface.
- Built with Python and Streamlit.
- Handles empty text input.
- Includes basic error handling and retry logic.
- Keeps the API key in an environment file instead of hardcoding it in the source code.

## Technologies Used
- Python
- Google Gemini API
- Streamlit
- python-dotenv

## Project Files
- `app.py` — Provides the web interface.
- `ai.py` — Handles Gemini API requests and error handling.
- `requirements.txt` — Lists the required Python packages.
- `.env.example` — Shows the environment variable needed for the API key.
- `.gitignore` — Prevents sensitive and unnecessary files from being tracked by Git.

## Setup Instructions

### 1. Install the required packages

Open a terminal in the project directory and run:

```bash
python -m pip install -r requirements.txt
```

### 2. Configure your API key

Create a file named `.env` in the project directory.

Add your own Gemini API key:

```dotenv
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

**Important:** Never upload your `.env` file or actual API key to GitHub.

### 3. Run the application

Run the following command in the terminal:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## How to Use
1. Open the application.
2. Paste text into the input box.
3. Click the **Summarize** button.
4. View the generated summary.

## Security
The API key is stored in an environment file and should not be shared publicly.

## Project Status
The application has been built and tested as part of an internship learning project.
