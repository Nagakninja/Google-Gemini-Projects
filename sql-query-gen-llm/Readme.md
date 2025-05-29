# SQL Query Generator and Executor using Google Gemini

This project is a Streamlit web application that enables users to ask questions in plain English, which are then converted into SQL queries using Google Gemini's generative AI. The generated SQL queries are executed on a sample SQLite database, and the results are displayed interactively in the web interface.

---

## Features

- **Natural Language to SQL**: Converts English questions into SQL queries using Google Gemini (`gemini-1.5-flash-latest`).
- **Automated Query Execution**: Runs the generated SQL against a pre-populated SQLite database (`student.db`).
- **Interactive Web UI**: Built with Streamlit for easy user interaction.
- **Sample Data Included**: The database contains a `STUDENT` table with example records for demonstration.

---

## How It Works

1. **Environment Setup**:  
   Loads environment variables (such as the Google API key) from a `.env` file using `python-dotenv`.

2. **Database Initialization**:  
   The [`sqlite.py`](sql-query-gen-llm/sqlite.py) script creates a `student.db` SQLite database with a `STUDENT` table and inserts sample records.

3. **AI-Powered SQL Generation**:  
   The main app ([`sql.py`](sql-query-gen-llm/sql.py)) uses Google Gemini to convert user questions into SQL queries, based on a carefully crafted prompt.

4. **Query Execution & Display**:  
   The generated SQL is executed on the database, and the results are shown in the Streamlit interface.

---

## File Structure
sql-query-gen-llm/ │ ├── .env # Environment variables (API keys) ├── .gitignore ├── requirements.txt # Python dependencies ├── sql.py # Main Streamlit application ├── sqlite.py # Script to initialize the database └── student.db # SQLite database file (auto-created)


---

## Database Schema & Sample Data

The `STUDENT` table is created with the following schema:

| Column  | Type         |
|---------|--------------|
| NAME    | VARCHAR(25)  |
| CLASS   | VARCHAR(25)  |
| SECTION | VARCHAR(25)  |
| MARKS   | INT          |

Sample records inserted:

| NAME      | CLASS        | SECTION | MARKS |
|-----------|--------------|---------|-------|
| John      | Data Science | A       | 90    |
| Alex      | Data Science | B       | 100   |
| Kelly     | Data Science | A       | 86    |
| Smita     | DEVOPS       | A       | 50    |
| Ayan      | DEVOPS       | A       | 45    |

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd sql-query-gen-llm
```    
### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then run:
```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a .env file in the sql-query-gen-llm directory with your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Initialize the Database
Run the database setup script to create student.db and populate it with sample data:
```sh
python sqlite.py
```

### 5. Run the Streamlit Application
Start the web app:
```sh
streamlit run sql.py
```
---

## Usage
- Open the Streamlit app in your browser (the URL will be shown in the terminal).
- Enter a question in plain English (e.g., "List all students in Data Science class").
- Click "Ask the question".
- The app will:
    - Use Gemini to generate the corresponding SQL query.
    - Execute the query on the student.db database.
    - Display the results in the app.

---

### Example
#### Input:
```sh
How many students are in the Data Science class?
```

#### Generated SQL:
```sql
SELECT COUNT(*) FROM STUDENT WHERE CLASS="Data Science";
```

#### Output:
The count of students in the Data Science class.

---

### Code Overview
**[sqlite.py](./sqlite.py)**

- Connects to (or creates) student.db.
- Creates the STUDENT table.
- Inserts sample records.
- Prints all inserted records for verification.

**[sql.py](./sql.py)**

- Loads environment variables and configures the Gemini API.
- Defines a prompt to instruct Gemini to generate SQL for the STUDENT table.
- Provides:
    - get_gemini_response(question, prompt): Calls Gemini to generate SQL.
    - read_sql_query(sql, db): Executes SQL on the SQLite database and returns results.
- Streamlit UI for user input and displaying results.

---

### Notes

- The app is for demonstration and educational purposes.
- Generated SQL is executed directly; in production, always validate and sanitize AI-generated queries.
- The database is recreated each time you run sqlite.py, overwriting previous data.

---

### License

MIT License (add your details as needed)

---

### Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [SQLite](https://sqlite.org)