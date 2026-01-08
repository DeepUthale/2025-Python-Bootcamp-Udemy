from openai import OpenAI

OPENAI_API_KEY = "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"

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
