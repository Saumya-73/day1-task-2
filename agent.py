from config import client, MODEL
from tools import get_course_fee, calculate_total


def run_agent(user_input):
    print("\nAgent started...")

    # Ask the LLM to decide what to do
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a college course fee assistant. "
                    "Use the available tools when course fee information is needed."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_course_fee",
                    "description": "Get the fee of a college course.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "course_code": {
                                "type": "string",
                                "description": "Course code such as CS101, AI202, or DS303"
                            }
                        },
                        "required": ["course_code"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "calculate_total",
                    "description": "Calculate total of two course fees after 10 percent discount.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "fee1": {
                                "type": "number"
                            },
                            "fee2": {
                                "type": "number"
                            }
                        },
                        "required": ["fee1", "fee2"]
                    }
                }
            }
        ]
    )

    message = response.choices[0].message

    # Tool call
    if message.tool_calls:
        for tool_call in message.tool_calls:

            if tool_call.function.name == "get_course_fee":
                course_code = eval(tool_call.function.arguments)["course_code"]

                result = get_course_fee(course_code)

                print("Tool used: get_course_fee")
                print("Tool result:", result)

                return f"The fee for {course_code} is ₹{result}."

    return message.content


print("College Course Fee - AI Agent")
print("Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    print("Agent:", run_agent(user_input))