from openai import OpenAI

OPENAI_API_KEY = "API_KEY"

messages = []

client = OpenAI(
    # This is the default and can be omitted
    api_key = OPENAI_API_KEY,
) 

def completion(message):
    global messages
    messages.append(
        {
            "role" : "user",
            "content" : message, 
        }
    )

    chat_completion = client.chat.completions.create(
            messages = messages,
            model = "gpt-4o",
    )
    # print(chat_completion)
    message = {
        "role" : "assistant",
        "content" : chat_completion.choices[0].message.content,
    }
    messages.append(message)
    print(f"AI: {message["content"]}")

if __name__ == "__main__":
    print(f"AI: Hi! I am AI, How may I help you?")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)

