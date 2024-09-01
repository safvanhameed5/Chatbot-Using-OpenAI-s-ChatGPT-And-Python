from openai import OpenAI
import argparse  # Make sure your api.py correctly returns your API key  # Set your OpenAI API key

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="private key",
)

# Main function to handle the chatbot conversation
def main():
    parser = argparse.ArgumentParser(
        description="Simple command line chatbot with GPT-4"
    )
    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the chatbot's personality",
        default="friendly and helpful",
    )
    args = parser.parse_args()

    initial_prompt = (
        f"You are a conversational chatbot. Your personality is: {args.personality}"
    )
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            # Take user input and format it
            user_input = input("You: ")
            messages.append({"role": "user", "content": user_input})

            # Create a chat completion request with the correct format
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Use "gpt-4" or "gpt-3.5-turbo"
                messages=messages,
                max_tokens=5,  # Adjust max_tokens as needed for longer responses
                temperature=0,  # Optional: Adjust the creativity of the response
            )

            # Extract and print the assistant's response
            assistant_message = response['choices'][0]['message']['content']
            messages.append({"role": "assistant", "content": assistant_message})
            print("Assistant: ", assistant_message)

        except KeyboardInterrupt:
            print("\nExiting...")  # Handles Ctrl+C gracefully
            break
        except Exception as e:
            print(f"An error occurred: {e}")  # Catch all other exceptions for debugging

# Entry point of the script
if __name__ == "__main__":
    main()
