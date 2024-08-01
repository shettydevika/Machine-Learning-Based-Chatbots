import joblib

# Load the model
model = joblib.load('chatbot_model.pkl')

def get_response(user_input):
    response = model.predict([user_input])[0]
    return response

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
