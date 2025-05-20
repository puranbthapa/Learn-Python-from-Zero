import openai
from dotenv import load_dotenv
import os

def chat_with_gpt():
    """
    Function to interact with OpenAI GPT API using the updated interface.
    """
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: API key not found. Please add it to a .env file.")
        return

    openai.api_key = api_key

    print("\nWelcome to GPT Chat! Type 'exit' to quit.\n")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Append user message
            messages.append({"role": "user", "content": user_input})

            # Sending the input to GPT API using the correct interface
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=messages
            )

            # Extracting the reply from the response
            gpt_reply = response['choices'][0]['message']['content']

            # Append assistant message
            messages.append({"role": "assistant", "content": gpt_reply})

            print(f"GPT: {gpt_reply}\n")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_gpt()
