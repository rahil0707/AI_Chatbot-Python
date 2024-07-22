from openai import OpenAI

openai = OpenAI(
    api_key='fake_api_key',
)

def chat_with_gpt(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    response = openai.chat.completions.create(
        messages=[message],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit" or user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    chat()