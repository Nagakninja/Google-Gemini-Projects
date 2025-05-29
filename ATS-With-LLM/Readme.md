# Smart ATS (Applicant Tracking System) with Google Gemini

A Streamlit-powered web application that uses Google Gemini LLM to analyze and score resumes against job descriptions. The app extracts text from uploaded PDF resumes, sends it along with the job description to Gemini, and parses the AI's structured response to display a summary, JD match percentage, and missing keywords.

---

## Features

- **Resume Upload:** Upload your resume as a PDF.
- **Job Description Input:** Paste the job description for your target role.
- **AI-Powered Analysis:** Uses Google Gemini (`gemini-2.0-flash`) to evaluate your resume.
- **Structured Output:** Displays a profile summary, JD match percentage, and missing keywords.
- **Modern UI:** Results are shown in visually distinct containers for clarity.

---

## How It Works

1. **PDF Extraction:**  
   The app reads all text from the uploaded PDF resume using PyPDF2.

2. **Prompt Engineering:**  
   The resume text and job description are formatted into a prompt for Gemini, requesting a structured JSON-like response.

3. **LLM Evaluation:**  
   Gemini analyzes the resume and job description, returning a string with JD match percentage, missing keywords, and a profile summary.

4. **Parsing & Display:**  
   The response is parsed using a Pydantic model ([`ProfileSummary.ProfileAnalysis`](ProfileSummary.py)), and results are shown in Streamlit with styled containers.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd ATS-With-LLM
```

### 2. Install Dependencies

Make sure you have Python 3.8+ installed. Then run:

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Run the Application

```sh
streamlit run app.py
```

---

## Usage

1. Open the Streamlit app in your browser (the URL will be shown in the terminal).
2. Paste the job description in the text area.
3. Upload your resume as a PDF file.
4. Click **Submit**.
5. View your profile summary, JD match percentage, and missing keywords in styled containers.

---

## File Structure

```
ATS-With-LLM/
│
├── app.py
├── ProfileSummary.py
├── requirements.txt
├── .env
└── .gitignore
```

- **app.py**: Main Streamlit application.
- **ProfileSummary.py**: Pydantic model for parsing Gemini's response.
- **requirements.txt**: Python dependencies.

---

## Notes

- Only PDF resumes are supported.
- The app uses Google Gemini (`gemini-2.0-flash`) for all AI evaluations.
- The output structure is enforced using Pydantic for reliability.
- Results are displayed in light gray containers for readability.

---

## License

MIT License (add your details as needed)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [Pydantic](https://docs.pydantic.dev/)