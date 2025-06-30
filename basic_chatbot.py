# Step 1: Let user define responses
print("Welcome to your custom chatbot!")
num_rules = int(input("How many responses do you want to define? "))

response_rules = {}

for _ in range(num_rules):
    question = input("Enter a user message (e.g., hello): ").lower()
    reply = input(f"Enter the bot's reply to '{question}': ")
    response_rules[question] = reply

# Step 2: Chat loop
print("\nChatbot is ready! Type 'bye' to exit.\n")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Bot: Goodbye!")
        break
    elif user_input in response_rules:
        print("Bot:", response_rules[user_input])
    else:
        print("Bot: I don't understand that.")
