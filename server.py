import os

import openai
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from openai import OpenAI
app = Flask(__name__)

# Initialize OpenAI with your API key
api_key = f'{os.getenv("token")}'
# client = openai.Client(api_key=api_key)
def parse_html(raw_html):
    # Parse the raw HTML to extract meaningful text
    soup = BeautifulSoup(raw_html, 'html.parser')

    # Extract text from all paragraphs, headers, etc. (customize as per your needs)
    paragraphs = soup.find_all(["main","article","ul","li",'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    cleaned_text = []
    for paragraph in paragraphs:
        cleaned_text.append(paragraph.get_text().strip())

    # Join all extracted text into a single string
    cleaned_content = "\n".join(cleaned_text)

    return cleaned_content
# from transformers import pipeline
# oracle = pipeline(model="deepset/roberta-base-squad2")
import google.generativeai as genai
import os
def get_response(code, message, First):
    context = "you are a Specific Ai that is here to help a person understanding a web page and answering the questions based in the html content of the page."
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    modal = genai.chat(model='models/chat-bison-001',
                       temperature=0.25,
                       top_p=0.95,
                       top_k=40, context=context,
                       messages=f"Based on the given HTML code ,Answer the question,HTML:{code},question:{message}")
    if First == True:
        return modal.messages[-1]
    else:
        return modal.reply(message).messages[-1]
count = 0
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    content = data.get('content')
    question = data.get('question')
    print(content)
    content = parse_html(content)
    response = ""
    if count==0:
        response = get_response(content,question,True)
    else:
        response = get_response(content,question,First=False)
    # question += " provide a full sentence answer."
    cleaned_content = content
    # message = f"Based on the following content, answer the question:\n\nContent: {cleaned_content}\n\nQuestion: {question}\n\nAnswer:"
    # print(cleaned_content)
    # API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
    # headers = {"Authorization": f"Bearer {os.environ.get('token')}"}
    #
    # # Make the GET request
    # response = requests.post(API_URL, headers=headers, json=message)
    # response = response.json()
    # print(response)
    return jsonify({'answer': response['content']})


if __name__ == '__main__':
    app.run(debug = True,port=5000)

