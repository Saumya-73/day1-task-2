from config import client, MODEL

print("College Course Fee Chatbot")
print("Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a simple college course fee chatbot. "
                    "Answer general questions about college course fees. "
                    "You do not have direct access to private course fee data."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("Chatbot:", response.choices[0].message.content)