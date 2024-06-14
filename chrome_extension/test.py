import os

import requests
# from transformers import pipeline
# oracle = pipeline(model="deepset/roberta-base-squad2")
content = "anup is a name of a person.He likes to play badminton.his badminton court is near his office where he works . and the office is on MG road."
question = "what are the things near MG road"
question +=" answer this based on the html context provided and general knowledge from the training. provide a full sentence answer."
# answer = oracle(question=question, context=content)
# # answer = "this is very good ."
# print(answer)
# generator = pipeline(model="text2text-generation")
# hee = generator(question = question,content = content)
# print(hee)
# pip install bitsandbytes accelerate
# from transformers import T5Tokenizer, T5ForConditionalGeneration
#
# tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
# model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl", device_map="auto", load_in_8bit=True)
#
# input_text = "translate English to German: How old are you?"
# input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
#
# outputs = model.generate(input_ids)
# print(tokenizer.decode(outputs[0]))
message = f"Based on the following content, answer the question:\n\nContent: {content}\n\nQuestion: {question}\n\nAnswer:"
# Define the URL and headers
# url = 'https://api.openai.com/v1/models'
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": f"Bearer {os.environ.get('token')}"}



# Make the GET request
response = requests.post(API_URL, headers=headers, json=message)

# answer = response.json()
print(response.json())
