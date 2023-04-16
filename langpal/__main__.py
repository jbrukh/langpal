from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def main():
    chat = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")
    while True:
        text = input('\n> ')
        msg = HumanMessage(content=text)
        result = chat([msg])
        print('\n', result.content)

if __name__ == "__main__":
    main()