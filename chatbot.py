# Install the OpenAI library
!pip install openai --quiet

# Import required modules
import openai
import getpass
import IPython

# Set OpenAI API Key
api_key = getpass.getpass("Enter your OpenAI API key: ")
openai.api_key = api_key

# Define available AI personalities
ai_personalities = {
    "1": ("Romantic", "You are a poetic and romantic AI that writes with affection and emotion."),
    "2": ("Coding", "You are a professional programming assistant. Answer questions with clarity and code examples."),
    "3": ("Journaling", "You are a thoughtful and reflective journaling guide that helps users explore their feelings."),
    "4": ("Exercise", "You are a motivating fitness coach that helps users stay healthy and active."),
    "5": ("Spiritual", "You are a peaceful and wise spiritual guide offering calm advice."),
    "6": ("Productivity", "You are a sharp productivity coach who helps people plan their day effectively."),
    "7": ("Comedian", "You are a witty stand-up comedian who makes funny and clever replies."),
    "8": ("Career Coach", "You help users with resume tips, interviews, and career growth advice."),
    "9": ("Therapist", "You are a warm and compassionate therapist that listens and helps.")
}

# Display options
print("Choose the type of AI you want to chat with:")
for key, (name, _) in ai_personalities.items():
    print(f"{key}. {name}")

# Get user choice
choice = input("Enter the number of your chosen AI type: ")

# Validate and get system message
if choice in ai_personalities:
    role_name, system_prompt = ai_personalities[choice]
else:
    print("Invalid choice. Defaulting to Coding Assistant.")
    role_name, system_prompt = ai_personalities["2"]

print(f"\nYou are now chatting with the '{role_name}' AI.\n")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye! 👋")
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response['choices'][0]['message']['content']
    print(f"{role_name} AI: {reply}\n")
