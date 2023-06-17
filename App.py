from apikey import apikey 
import os
os.environ['OPENAI_API_KEY'] = apikey
import openai
import streamlit as st 



def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


# Streamlit app layout
st.title("Order Bot")
st.write("Hello! Welcome to the pizza restaurant. say hi to start conversation ")

# Initialize conversation messages
messages = [
    {'role': 'system', 'content': """
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""},
    {'role': 'assistant', 'content': 'say Hi, you are OrderBot, say how may i help you?'}
]

# User input
user_input = st.text_input("You: ")

# Handle user input
if st.button("Submit"):
    messages.append({'role': 'user', 'content': f'"{user_input}"'})
    response = get_completion_from_messages(messages, temperature=1)
    messages.append({'role': 'assistant', 'content': f'"{response}"'})
    st.text_area("Bot:", value=response, height=200)

# Display conversation history
st.subheader("Conversation History")
for i, message in enumerate(messages):
    if message['role'] == 'user':
        st.text_area("You:", value=message['content'], height=80)
    elif message['role'] == 'assistant':
        st.text_area("Bot:", value=message['content'], height=80)
    if i < len(messages) - 1:
        st.write("---")