# YouTube Transcript to Detailed Notes Converter

A Streamlit web application that uses Google Gemini to automatically extract, summarize, and present detailed notes from YouTube video transcripts. Simply provide a YouTube video link, and the app will fetch the transcript, summarize the content using Gemini, and display the key points in an easy-to-read format.

---

## Features

- **YouTube Transcript Extraction:**  
  Automatically fetches the transcript of any YouTube video (if available) using the video URL.

- **AI-Powered Summarization:**  
  Uses Google Gemini (`gemini-2.0-flash-exp`) to generate a concise, point-wise summary of the video transcript.

- **Visual Preview:**  
  Displays the video thumbnail for quick visual confirmation.

- **Interactive Web UI:**  
  Built with Streamlit for a simple and user-friendly experience.

---

## How It Works

1. **Environment Setup:**  
   Loads environment variables (such as your Google API key) from a `.env` file using `python-dotenv`.

2. **Transcript Extraction:**  
   Uses the `youtube_transcript_api` to fetch the transcript text from the provided YouTube video link.

3. **Summarization:**  
   Sends the transcript to Google Gemini with a prompt to generate a summary in bullet points (within 300 words).

4. **Display:**  
   Shows the video thumbnail and the AI-generated summary in the Streamlit app.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd YTtanscriber
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
2. Enter a YouTube video link in the input box.
3. The app will display the video thumbnail.
4. Click **"Get Detailed Notes"**.
5. View the AI-generated summary of the video transcript.

---

## File Structure

```
YTtanscriber/
│
├── app.py
├── requirements.txt
├── .env
└── .gitignore
```

---

## Notes

- The app only works with YouTube videos that have transcripts available.
- All AI summarization is performed using Google Gemini (`gemini-2.0-flash-exp`).
- The summary is limited to 300 words and presented in bullet points for clarity.

---

## License

MIT License (add your details as needed)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)