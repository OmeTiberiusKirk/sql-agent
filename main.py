from agent import AIAgent
from ollama import chat


def main():
    agent = AIAgent()

    # print("AI Agent initialized. Type 'quit' to exit.")

    # while True:
    #     user_input = input("You: ")

    #     if user_input.lower() == "quit":
    #         break

    #     print(user_input)
    #     agent.generate_response(user_input)

    agent.close()


if __name__ == "__main__":
    main()
