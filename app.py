import asyncio
import sys
from g4f.client import Client

# Set the event loop policy for Windows
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Initialize the client
client = Client()

# Function to get a response from the GPT model
def get_gpt_response(user_message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
    )
    return response.choices[0].message.content

# Main interaction loop
if __name__ == "__main__":
    print("User: Hi GTP!")
    print("GTP: I am here to assist you.")
    
    while True:
        # Get input from the user
        user_message = input("User: ")
        
        # Get response from GPT model
        gpt_response = get_gpt_response(user_message)
        
        # Print the response
        print(f"GTP: {gpt_response}")
