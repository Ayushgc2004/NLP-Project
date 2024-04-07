import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

# Load the pre-trained question answering pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def get_pdf_text(pdf_files):
    pdf_texts = []
    for pdf_file in pdf_files:
        text = ""
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
        pdf_texts.append((pdf_file.name, text))
    return pdf_texts 

def main():
    st.title("PDF Question Answering System")

    # Sidebar for uploading PDF files
    st.sidebar.title("Upload PDF")
    pdf_files = st.sidebar.file_uploader("Upload PDF files", accept_multiple_files=True, type=["pdf"])

    # Main window for entering question
    st.header("Enter your question:")
    question = st.text_input("Type your question here")

    if not pdf_files:
        st.write("No PDF file uploaded.")
    elif pdf_files and question:
        max_score = float('-inf')
        best_answer = None
        best_pdf_name = None

        # Extract text from PDF files
        pdf_texts = get_pdf_text(pdf_files)

        # Iterate over each PDF text
        for pdf_name, pdf_text in pdf_texts:
            # Get answer using the pre-trained model
            answer = qa_pipeline(question=question, context=pdf_text)

            # Update max_score and best_answer if the current answer has higher score
            if answer['score'] > max_score:
                max_score = answer['score']
                best_answer = answer
                best_pdf_name = pdf_name

        if best_answer:
            # Display answer with the highest confidence score
            st.subheader(f"Answer from {best_pdf_name}:")
            st.write(best_answer['answer'])
            st.subheader("Confidence Score:")
            st.write(best_answer['score'])
        else:
            st.write("No answer found.")

if __name__ == "__main__":
    main()
