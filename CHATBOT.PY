import openai

# Set your OpenAI API key here
api_key = "YOUR_API_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_gpt(prompt):
    # Define the system message (introduction)
    system_message = "You are a helpful assistant."

    # Create a list of messages, including the system message and user input
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    # Send the messages to the ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract and return the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

# Start a conversation with GPT-3
print("Hello! I'm your chatbot. You can chat with me. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    assistant_response = chat_with_gpt(user_input)
    print("Chatbot:", assistant_response)
