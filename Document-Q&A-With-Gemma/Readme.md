# Document-Q&A-With-Gemma

A Streamlit web application that enables users to perform question answering (Q&A) over a collection of PDF documents using advanced AI models. The app leverages Google Gemini for embeddings, FAISS for vector storage and retrieval, and Groq's Llama3 for generating answers.

---

## Features

- **PDF Directory Loader:** Automatically loads all PDF files from the `us_census/` directory.
- **Text Chunking:** Splits PDF content into manageable chunks for efficient retrieval.
- **Vector Embedding:** Uses Google Generative AI embeddings to convert text chunks into vectors.
- **FAISS Vector Store:** Stores embeddings in a FAISS vector database for fast similarity search.
- **Conversational Q&A:** Answers user questions based strictly on the provided document context using Groq's Llama3 model.
- **Document Similarity Display:** Shows the most relevant document chunks used to answer each question.

---

## How It Works

1. **Environment Setup**
   - Loads environment variables (API keys) from a `.env` file using `python-dotenv`.
   - Configures both Google Gemini and Groq API keys.

2. **PDF Loading and Processing**
   - Loads all PDF files from the `us_census/` directory using `PyPDFDirectoryLoader`.
   - Extracts and splits text into chunks with `RecursiveCharacterTextSplitter`.

3. **Vector Embedding and Storage**
   - Embeds text chunks using Google Generative AI embeddings (`models/embedding-001`).
   - Stores the embeddings in a FAISS vector database for similarity search.

4. **Conversational Chain Setup**
   - Defines a prompt template instructing the model to answer strictly from the provided context.
   - Uses Groq's Llama3 model for generating answers.

5. **Question Answering**
   - Users enter questions in the input box.
   - The app retrieves the most relevant chunks from the FAISS store.
   - The Llama3 model generates an answer based on the retrieved context.
   - Displays both the answer and the relevant document chunks.

---

## Code Overview

### Main Components

- **`vector_embedding()`**
  - Loads PDFs, splits them into chunks, embeds them, and stores vectors in session state.

- **`ChatGroq`**
  - Initializes the Llama3 model for generating answers.

- **`ChatPromptTemplate`**
  - Defines the prompt for the Q&A chain.

- **Streamlit UI**
  - Button to trigger document embedding.
  - Input box for user questions.
  - Displays answers and relevant document chunks.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd Document-Q&A-With-Gemma
```

### 2. Install Requirements

Ensure you have Python 3.8+ installed. Then install dependencies:

```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root with your API keys:

```
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Add PDF Documents

Place your PDF files in the `us_census/` directory. Sample files are already included.

### 5. Run the Streamlit App

```sh
streamlit run app.py
```

---

## Usage

1. Click the **"Documents Embedding"** button to process and embed the PDFs.
2. Enter your question in the input box.
3. The app will display the answer and show the most relevant document chunks used for the answer.

---

## File Structure

```
Document-Q&A-With-Gemma/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── us_census/
│   ├── acsbr-015.pdf
│   ├── acsbr-016.pdf
│   ├── acsbr-017.pdf
│   └── p70-178.pdf
```

---

## Notes

- All answers are strictly based on the content of the uploaded PDFs.
- Embeddings and vector storage are handled in memory/session state.
- The app uses Groq's Llama3 model for generating answers and Google Gemini for embeddings.

---

## License

MIT License (add your details as needed)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Google Generative AI](https://ai.google.dev/)
- [FAISS](https://faiss.ai/)
- [Groq](https://groq.com/)