# ATS Resume Expert (Applicant Tracking System)

A Streamlit web application that leverages Google Gemini Vision to analyze and evaluate resumes (PDFs) against job descriptions. The app converts uploaded resumes into images, sends them to Gemini for analysis, and provides both qualitative feedback and a percentage match with missing keywords.

---

## Features

- **Resume Upload:** Upload your resume in PDF format.
- **Job Description Input:** Paste or type the job description for the target role.
- **AI-Powered Evaluation:** Uses Google Gemini Vision (`gemini-2.0-flash-exp`) to analyze the resume.
- **Professional Review:** Get a detailed HR-style evaluation of strengths and weaknesses.
- **ATS Percentage Match:** See how well your resume matches the job description, including missing keywords and final thoughts.
- **User-Friendly Interface:** Built with Streamlit for easy interaction.

---

## How It Works

1. **Environment Setup:**  
   Loads environment variables (such as your Google API key) from a `.env` file using `python-dotenv`.

2. **Resume Processing:**  
   - Converts the first page of the uploaded PDF resume into a JPEG image.
   - Encodes the image in base64 for Gemini API compatibility.

3. **Gemini Vision Integration:**  
   - Sends the job description, resume image, and a prompt to Gemini Vision.
   - Receives a detailed evaluation or percentage match as a response.

4. **Streamlit UI:**  
   - Input for job description.
   - File uploader for resume PDF.
   - Buttons to trigger evaluation or percentage match.
   - Displays the AI-generated feedback in the app.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd ATS-System
```

### 2. Install Requirements

Make sure you have Python 3.8+ installed. Then run:

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Run the Streamlit Application

```sh
streamlit run app.py
```

---

## Usage

1. Open the Streamlit app in your browser (the URL will be shown in the terminal).
2. Enter the job description in the provided text area.
3. Upload your resume as a PDF file.
4. Click **"Tell Me About the Resume"** for a professional HR-style evaluation.
5. Click **"Percentage match"** to see the ATS match percentage, missing keywords, and final thoughts.

---

## File Structure

```
ATS-System/
│
├── app.py
├── requirements.txt
├── .env
└── .gitignore
```

---

## Notes

- Only the first page of the resume PDF is analyzed.
- The app uses Google Gemini Vision (`gemini-2.0-flash-exp`) for all AI-powered evaluations.
- All processing is done locally except for the AI analysis, which uses the Gemini API.
- For best results, ensure your resume is clear and well-formatted.

---

## License

MIT License (add your details as needed)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [pdf2image](https://github.com/Belval/pdf2image)
- [Pillow](https://python-pillow.org/)