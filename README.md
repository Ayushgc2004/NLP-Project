# PDF Question Answering System

We have developed a "QUESTION ANSWERING SYSTEM" model in which we have to upload a pdf file and ask a question and then by processing it will give us the answer according to the question asked.

We have used a pretrained model called "distilbert-base-cased-distilled-squad" for training our model.This model has been trained on a large dataset which is of approx 400MB.This model have approximately 500k tokens and this tokens will help us in finding the correct answer for the question.

In our model,the working is as follows:
1. Pdf file is entered as an input.
2. The data of this pdf fiile is converted to text.
3. The context is divided into tokens and the stopwords are removed from it.
4. Multiple questions can be asked.
5. For finding the answer,we will find the start index and end index from the context that is used for answering the question.

In this way,we will find the answer to a question

# Streamlit App

We have developed a basic streamlit app in which we will be giving the pdf file for context.
Then the question is entered.Based on the model and processing,it will provide an answer.In this we have also added an option of uploading a multiple files and the answer is generated from the particular file.

In this way,we have developed a question answering system.
