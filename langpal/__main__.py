from langchain.llms import OpenAI


def main():
    llm = OpenAI(temperature=0.9, model_name="gpt-3.5-turbo")
    while True:
        text = input('\n> ')
        print(llm(text))

if __name__ == "__main__":
    main()