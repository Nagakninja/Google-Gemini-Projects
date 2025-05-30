# Calories Advisor App

A Streamlit-based Health Management application that uses Google Gemini Vision to analyze food images, estimate total calories, and provide nutritional breakdowns. Upload a food image and get instant AI-powered insights into calorie content and healthiness.

---

## Features

- **Image Upload:** Upload images of food in JPG, JPEG, or PNG format.
- **AI-Powered Analysis:** Uses Google Gemini Vision (`gemini-2.0-flash-exp`) to analyze the food items in the image.
- **Calorie Estimation:** Returns total calories and a breakdown of calories per food item.
- **Nutritional Breakdown:** Provides the percentage split of carbohydrates, fats, fibers, sugar, and other nutrients.
- **Health Assessment:** Indicates whether the food is healthy or not.

---

## How It Works

1. **Image Upload:**  
   Users upload a food image via the Streamlit interface.

2. **Image Processing:**  
   The image is read and prepared for the Gemini API.

3. **Prompt Engineering:**  
   The app sends a prompt and the image to Gemini, asking for calorie and nutrition analysis.

4. **AI Response:**  
   Gemini returns a structured response with calorie counts, nutritional breakdown, and a health assessment.

5. **Display:**  
   The results are displayed in the Streamlit app for easy review.

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repository-url>
cd HealthApp
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
streamlit run health.py
```

---

## Usage

1. Open the Streamlit app in your browser (the URL will be shown in the terminal).
2. Upload a food image (JPG, JPEG, or PNG).
3. Click **"Tell me the total calories"**.
4. View the AI-generated calorie and nutrition analysis.

---

## File Structure

```
HealthApp/
│
├── health.py
├── requirements.txt
├── .env
├── .gitignore
└── data/
    ├── Image-1_Chicken-Picata.png
    ├── Image-2_Baked-Vegetable.png
    ├── Image-3_Chole-Masala-Chickpea.png
    └── Image-6_Continental-Breakfast.png
```

---

## Notes

- Only image files (JPG, JPEG, PNG) are supported.
- The app uses Google Gemini Vision for all AI-powered analysis.
- Example food images are provided in the `data/` folder for testing.

---

## License

MIT License (add your details as needed)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [Pillow](https://python-pillow.org/)