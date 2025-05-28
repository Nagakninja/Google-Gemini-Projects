# ChatWithPDF

A Streamlit web application that allows you to chat with the contents of your PDF files using Google Gemini's generative AI. The app leverages LangChain for text processing and vector storage (FAISS), enabling you to upload PDFs, process their content, and ask questions about them interactively.

---

## Features

- **Upload Multiple PDFs:** Supports uploading and processing multiple PDF files at once.
- **Text Extraction:** Extracts text from all pages of the uploaded PDFs.
- **Chunking:** Splits extracted text into manageable chunks for efficient retrieval.
- **Vector Store:** Uses FAISS to create and store vector embeddings of text chunks.
- **Conversational QA:** Asks questions about the PDF content and receives detailed answers powered by Google Gemini (`gemini-2.0-flash`).
- **Context-Aware Responses:** Ensures answers are based strictly on the provided PDF context.

---

## How It Works

1. **Environment Setup**
   - Loads environment variables (such as your Google API key) from a `.env` file using `python-dotenv`.
   - Configures the Google Gemini API with your API key.

2. **PDF Upload and Text Extraction**
   - Users upload one or more PDF files via the sidebar.
   - The app reads each PDF and extracts text from every page.

3. **Text Chunking**
   - The extracted text is split into overlapping chunks using LangChain's `RecursiveCharacterTextSplitter` for better context retrieval.

4. **Vector Embedding and Storage**
   - Each text chunk is embedded using Google Generative AI embeddings.
   - The embeddings are stored in a FAISS vector database for fast similarity search.

5. **Conversational Chain Setup**
   - A prompt template is defined to instruct the Gemini model to answer questions based only on the provided context.
   - LangChain's QA chain is loaded with the Gemini model and the custom prompt.

6. **Question Answering**
   - Users enter questions in the main input box.
   - The app retrieves the most relevant text chunks from the FAISS store.
   - The Gemini model generates a detailed answer based on the retrieved context.

---

## Code Overview

### Main Functions

- **`get_pdf_text(pdf_docs)`**  
  Extracts and concatenates text from all uploaded PDF files.

- **`get_text_chunks(text)`**  
  Splits the extracted text into overlapping chunks for better context retrieval.

- **`get_vector_store(text_chunks)`**  
  Embeds the text chunks and saves them in a FAISS vector store.

- **`get_conversational_chain()`**  
  Sets up the LangChain QA chain with a custom prompt and the Gemini model.

- **`user_input(user_question)`**  
  Retrieves relevant chunks for the user's question and generates an answer using the conversational chain.

- **`main()`**  
  Streamlit app entry point: handles UI, file uploads, processing, and user interaction.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd ChatWithPDF
```

### 2. Install Requirements

Make sure you have Python 3.8+ installed. Then install dependencies:

```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root with your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Run the Streamlit App

```sh
streamlit run app.py
```

### 5. Usage

- Use the sidebar to upload one or more PDF files and click "Submit & Process".
- Once processed, enter your question in the main input box.
- The app will display a detailed answer based on the PDF content.

---

## File Structure

```
ChatWithPDF/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── data/
│   └── (sample PDF files)
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
```

---

## Notes

- The app uses Google Gemini's `gemini-2.0-flash` model for question answering.
- All answers are strictly based on the content of the uploaded PDFs.
- Vector storage is handled locally using FAISS; indexes are saved in the `faiss_index/` directory.

---

## License

MIT License (add your license details here)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Google Generative AI](https://ai.google.dev/)
- [FAISS](https://faiss.ai/)