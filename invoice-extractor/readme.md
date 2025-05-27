# MultiLanguage Invoice Extractor

A Streamlit web application that uses Google Gemini's generative AI to extract and answer questions about invoice images in multiple languages.

---

## Features

- **Upload Invoice Images:** Supports `.jpg`, `.jpeg`, and `.png` formats.
- **AI-Powered Extraction:** Uses Google Gemini Vision (`gemini-2.0-flash`) to analyze invoice images.
- **Custom Prompt Input:** Ask any question about the uploaded invoice.
- **Multi-language Support:** Designed to work with invoices in various languages.
- **User-Friendly Interface:** Built with Streamlit for easy interaction.

---

## How It Works

1. **Environment Setup**
   - Loads environment variables from a `.env` file using `python-dotenv`.
   - Configures the Google Gemini API with your API key.

2. **Model Initialization**
   - Loads the Gemini Vision model:
     ```python
     model = genai.GenerativeModel('gemini-2.0-flash')
     ```

3. **Image Upload and Display**
   - Uses Streamlit's `file_uploader` to let users upload invoice images.
   - Displays the uploaded image in the app.

4. **Prompt Input**
   - Users enter a custom prompt/question about the invoice.

5. **Image Processing**
   - Reads the uploaded image as bytes and prepares it for the Gemini API.

6. **AI Response**
   - Sends a system prompt, the image, and the user's question to Gemini.
   - Displays the AI-generated response in the app.

---

## Code Overview

### Main Functions

- **`get_gemini_response(input, image, user_prompt)`**  
  Sends the system prompt, image, and user question to Gemini and returns the response.

- **`input_image_details(uploaded_file)`**  
  Converts the uploaded file into the format required by Gemini (extracts bytes and MIME type).

### Streamlit App Flow

- Sets up the page and header.
- Accepts a user prompt and invoice image upload.
- Displays the uploaded image.
- On button click, processes the image and prompt, sends them to Gemini, and displays the response.

---

## Setup Instructions

### 1. Install the requirements

```sh
    pip install -r requirements.txt
```

### 2. Run Streamlit App
```sh
    streamlit run app.py 
```