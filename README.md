# MCQ Generator

## Project Overview
The MCQ Generator is a web application that automates the creation of multiple-choice questions (MCQs) from text documents. It is designed for educators, content producers, and anyone needing efficient MCQ generation. The MCQ Generator App presents a convenient solution for automating the creation of multiple-choice questions (MCQs) from your text materials. Whether you're an educator developing quizzes, a content producer designing evaluations, or someone in need of prompt and effective MCQ generation, this application is your go-to option!

Click this link to go to the MCQ-GENERATOR web app: [MCQ Generator App](https://mcq-generator-djrn.onrender.com)

### Features
- **Document Upload:** Supports PDF and Word file uploads.
- **MCQ Generation:** Creates MCQs based on the content of uploaded documents.
- **Customization:** Allows specifying the number of MCQ pairs to generate.
- **Download:** Provides the generated MCQs in a downloadable Word document.

## Technologies Used
- **Programming Languages:** Python
- **Libraries and Frameworks:** Streamlit, Firebase, langchain, langchain_google_genai, dotenv, PyPDF2, python-docx
- **Cloud Platform:** Google Cloud Platform (for Firebase)

## NLP Algorithm
Utilizes pre-trained language models through the ChatGoogleGenerativeAI model from langchain_google_genai to generate MCQs.

## Document Parsing
- **PDF Parsing:** Uses PyPDF2 to extract text from PDF files.
- **Word Parsing:** Uses python-docx to extract text from Word documents.

## User Authentication
Implemented using Firebase Authentication for secure user sign-up and login.

## Streamlit Interface
Uses Streamlit to create an interactive web interface, allowing users to upload documents, customize MCQ generation, and download the results.

## Error Handling
Includes robust error handling to detect, log, and display informative error messages.

## MCQ Generation Process
Parses uploaded documents, extracts text, and generates specified MCQ question-answer pairs.

## Deployment
The application is deployed on Render. You can access it [here](https://mcq-generator-djrn.onrender.com).
