# import os
#
# import requests
# # from transformers import pipeline
# # oracle = pipeline(model="deepset/roberta-base-squad2")
# content = "anup is a name of a person.He likes to play badminton.his badminton court is near his office where he works . and the office is on MG road."
# question = "what are the things near MG road"
# question +=" answer this based on the html context provided and general knowledge from the training. provide a full sentence answer."
# # answer = oracle(question=question, context=content)
# # # answer = "this is very good ."
# # print(answer)
# # generator = pipeline(model="text2text-generation")
# # hee = generator(question = question,content = content)
# # print(hee)
# # pip install bitsandbytes accelerate
# # from transformers import T5Tokenizer, T5ForConditionalGeneration
# #
# # tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
# # model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl", device_map="auto", load_in_8bit=True)
# #
# # input_text = "translate English to German: How old are you?"
# # input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
# #
# # outputs = model.generate(input_ids)
# # print(tokenizer.decode(outputs[0]))
# message = f"Based on the following content, answer the question:\n\nContent: {content}\n\nQuestion: {question}\n\nAnswer:"
# # Define the URL and headers
# # url = 'https://api.openai.com/v1/models'
# API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
# headers = {"Authorization": f"Bearer {os.environ.get('token')}"}
#
#
#
# # Make the GET request
# response = requests.post(API_URL, headers=headers, json=message)
#
# # answer = response.json()
# print(response.json())
import google.generativeai

message = """<!DOCTYPE html>
<html>
<head>
  <title>Web Page Q&A</title>
  <style>
    /* Input box */
#question {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box; /* Ensures padding is included in width calculation */
}

/* Ask button */
#askButton {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease; /* Smooth transition on hover */
}

#askButton:hover {
  background-color: #0056b3;
}
#mydiv {
  /*position: absolute;*/
  width: 450px; /* Adjust width as needed */
  margin: 20px auto;
  /*background-color: #f0f0f0;*/
  /*border: 1px solid #ccc;*/
  /*border-radius: 8px;*/
  /*box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);*/
  /*font-family: Arial, sans-serif;*/
  /*padding: 20px; !* Adjust padding as needed *!*/
}
#mydivhead {
  width: 400px; /* Adjust width as needed */
  margin: 20px auto;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
  padding: 20px; /* Adjust padding as needed */
}



    </style>
</head>
<body>
<div id = "mydiv">
  <div id="mydivhead">
    <div id="header">
      <span id="header-text">Web Page Q&A</span>
      <span id="close-button">&times;</span>
    </div>
    <div id="content">
      <input type="text" id="question" placeholder="Ask a question...">
      <button id="askButton">Ask</button>
      <div id="answer"></div>
    </div>
    <div id="resizer"></div>
  </div>
  </div>
  <script src="popup.js"></script>
</body>
</html>
"""
import google.generativeai as genai
import PIL.Image
import os
context = "you are a general purpose Ai that will read html pages and give valid responses to the questions asked"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
img = PIL.Image.open('icon.jpg')
modal = genai.chat(model='models/chat-bison-001',
      temperature=0.25,
      top_p=0.95,
      top_k=40,context=context,messages=f"based on the given html answer the question,HTML:{message},question:{'what is the use of html tag'}")
# model = genai.GenerativeModel(model_name="")
# response = model.generate_content(["What is in this photo?", img])
print(modal.text)
# google.generativeai.chat()
# genai.