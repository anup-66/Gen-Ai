import os

import requests
from taipy.gui import Gui, State, notify
client = None
context = "This a general purpose ai assistent who can help in all the queries user asks.\n\Human: Hello, who are you ?\nAI:I am an Ai created by Anup.How can i help you today ?."

conv = {

    "conv": ["who are you ?",
                     "Hi, I am an Ai,How can i help you today."]

}
user_msg = ""
prev = []
selectedconv = None
row_selected = [1]
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
headers = {"Authorization": f"Bearer {os.environ.get('token')}"}

def query(text):
    response = requests.post(API_URL, headers=headers, json=text)
    return response.json()

import time
def request(state: State, prompt: str) -> str:
    output = query(
        {
            "inputs": prompt,
        }

    )
    print(output)
    return output[0]["generated_text"]

# def update_context(state: State)->str:
#     state.context += f"Human: \n {state.user_msg}\n\n AI:"
#     answer = request(state, state.context).replace("\n", "")
#     state.context += answer
#     state.row_selected = [len(state.conv["conv"])+1]
#     return answer

def send_message(state: State) -> None:
    state.context += f"Human: \n {state.user_msg}\n\n AI:"
    answer = request(state, state.context).replace("\n", "")
    state.context += answer
    state.row_selected = [len(state.conv["conv"])+1]
    conv = state.conv._dict.copy()
    conv["conv"] += [state.user_msg]
    state.conv = conv
    time.sleep(2)
    conv["conv"] += [answer]
    state.conv = conv
    state.user_msg = ""

def styling(state:State,idx:int,row:int)->str:
    if idx is None:
        return None
    elif idx%2==0:
        return "user_message"
    else:
        return "gpt_message"

def restore(state: State)->None:
    state.prev  = state.prev\
                                 + [[len(state.prev),state.conv]
                                 ]
    state.conv = {
        "conv": ["Who are you?", "Hi! I am An AI. How can I help you today?"]
    }

def tree_adapter(item: list) ->[str,str]:
    identifier = item[0]
    if len(item[1]["conv"])>3:
        return (identifier , item[1]["conv"][2][:50] + "...")
    return (item[0],"Empty conv")

def select_conv(state:State,var_name:str,value)->None:
    state.conv = state.prev[value[0][0]][1]
    state.context = "The following is a conv with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "
    for i in range(2, len(state.conv["conv"]), 2):
        state.context += f"Human: \n {state.conv['conv'][i]}\n\n AI:"
        state.context += state.conv["conv"][i + 1]
    state.row_selected = [len(state.conv["conv"]) + 1]
past_prompts = []

# page = """
# <|{conv}|table|show_all|style=styling|>
# <|{user_msg}|input|label=write...|on_action=send_message|class_name=fullwidth|>
# """
page = """
<|layout|columns=300px 1|
<|part|class_name=sidebar|
# **Chat Bot** # {: .logo-text}
<|New conversation|button|class_name=fullwidth new-conv-button|id=reset_app_button|on_action=restore|>
### Previous activities ### {: .h5 .mt2 .mb-half}
<|{selectedconv}|tree|lov={prev}|class_name=past_prompts_list|multiple|adapter=tree_adapter|on_change=select_conv|>
|>

<|part|class_name=p2 align-item-bottom table|
<|{conv}|table|style=styling|show_all|selected={row_selected}|rebuild|>
<|part|class_name=card mt1|
<|{user_msg}|input|label=Write your message here...|on_action=send_message|class_name=fullwidth|change_delay=-1|>
|>
|>
|>
"""
#     # <|{user_msg}|input|label=write your message here...|on_action=send_message|class_name=fullwidth|>
if __name__ == "__main__":
    Gui(page = page).run(dark_mode=False, title="Fisrt Taipy chatbot",use_reloader=True)


