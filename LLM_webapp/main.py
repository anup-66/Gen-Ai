import requests
from taipy.gui import Gui, State, notify
import token

context = "The Following is a conversation with an Ai assistant.The assistant is helpful , creative ,clever and very friendly.\n\Human: Hello, who are you ?\nAI:I am an Ai created by Anup.How can i help you today ?."

conversation = {

    "Conversation": ["who are you ?",
                     "Hi, I am an Ai,How can i help you today."]

}
current_user_message = ""
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
headers = {"Authorization": f"Bearer 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"}


# print(token)
# print(requests.post(API_URL, headers=headers, json={"inputs":"how are you."}).json())
def query(text):
    response = requests.post(API_URL, headers=headers, json=text)
    return response.json()


def request(state: State, prompt: str) -> str:
    output = query(
        {
            "inputs": prompt,
        }

    )
    print(output)
    return output[0]["generated_text"]


def send_message(state: State) -> None:
    state.context += f"Human: \n {state.current_user_message}\n\n AI:"
    answer = request(state, state.context).replace("\n", "")
    state.context += answer
    conv = state.conversation._dict.copy()
    conv["Conversation"] += [state.current_user_message, answer]
    state.conversation = conv
    state.current_user_message = ""


page = """
<|{conversation}|table|show_all|width=100%|>
<|{current_user_message}|input|label=write...|on_action=send_message|class_name=fullwidth|>
"""
#     # <|{current_user_message}|input|label=write your message here...|on_action=send_message|class_name=fullwidth|>
if __name__ == "__main__":
    Gui(page = page).run(dark_mode=True, title="Fisrt Taipy chatbot")

#
# from taipy.gui import Gui
#
# # x: [1..5]
# x_range = range(1, 6)
# data = {
#     "X": x_range,
#     "Y": [x*x for x in x_range]
# }
#
# column_orders = [("X;Y", "Squared"), ("Y;X", "Square root")]
# columns = column_orders[0]
#
# page = """
# <|{hello}|table|show_all|>
#
# <|{columns}|toggle|lov={column_orders}|>
# """

# Gui(page=page).run()