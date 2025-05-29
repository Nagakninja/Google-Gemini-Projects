import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import ProfileSummary
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        chat_input = input_prompt.format(text=text, jd=jd)
        response=get_gemini_repsonse(chat_input)
        parser = PydanticOutputParser(pydantic_object=ProfileSummary.ProfileAnalysis)
        profile_analysis=parser.parse(response)

        st.header("Profile Analysis")
        st.subheader("Summary")
        st.write(profile_analysis.profile_summary)
        
        st.subheader("JD Match: {}".format(profile_analysis.jd_match))
        with st.container():
            st.subheader("Missing Keywords")
            for keyword in profile_analysis.missing_keywords:
                st.markdown(
                    "<div display='flex' ><b><li>{}</div>".format(
                        keyword
                    ),
                    unsafe_allow_html=True,
                )