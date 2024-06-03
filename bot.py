import streamlit as st
import time
from llama2 import firePrompt

st.set_page_config(page_title='D BOT',
                   page_icon='💁🏻‍♂️',
                   layout='wide',
                   initial_sidebar_state='expanded'
                )

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'temp' not in st.session_state:
    st.session_state.temp = 0

with st.sidebar:
    st.image('dilak1.jpg',width=100)
 

# Assuming you have your zoom template functionality in a separate function
def zoom_template(zoom_factor):
    # Your code to implement the zoom template functionality using zoom_factor
    # This could involve scaling images, adjusting layout, etc.
    # ...
    pass

with st.sidebar:
    st.markdown('## ', unsafe_allow_html=True)

    # Improved slider with visible label and potentially a tooltip
    st.session_state.temp = st.slider(
        label='Zoom Level',  # Clear and descriptive label
        min_value=0.0,
        max_value=1.0,
        step=0.1,
        value=0.3,
        help="Adjust the zoom level of the visualization (0.0 - minimum, 1.0 - maximum)"  # Optional tooltip
    )

    # Add zoom in/out buttons or alternative controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Zoom In"):
            st.session_state.temp = min(1.0, st.session_state.temp + 0.1)  # Limit to max zoom
    with col2:
        if st.button("Zoom Out"):
            st.session_state.temp = max(0.0, st.session_state.state.temp - 0.1)  # Limit to min zoom

# Apply zoom based on session_state.temp in the main app body
zoom_template(st.session_state.temp)

with st.sidebar:
   st.image('dbot.png', use_column_width=True)
   st.markdown('## :rainbow[Powered by llama2 🦙🦙🦙 ] ', unsafe_allow_html=True)

def getAvatar(role):
    if role == 'assistant':
        return "dilak1.jpg"
    else :
        return "dbot.png"

def getContext():
    res = ""
    for item in st.session_state.messages[:-1]:
        res = res + f"role : {item['role']} content : {item['content']}\n"
    return res

st.markdown('# :rainbow[D]  :rainbow[BOT]🤖', unsafe_allow_html=True)


with st.chat_message(name="assistant", avatar='dbot.png'):
    st.markdown('#### Ask me anything!  ')
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=getAvatar(message["role"])):
        st.markdown(f'{message["content"]}')

if prompt := st.chat_input(placeholder="Chat with me."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(name="user", avatar='dbot.png'):
        st.markdown(prompt)
    with st.chat_message(name='assistant', avatar='dbot.png'):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner(text="Processing... ⏳⌛⏳"):
            raw = firePrompt(st.session_state.messages[-1]['content'], temp=st.session_state.temp)
            response = str(raw)
            # Simulate stream of response with milliseconds delay
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)
            message_placeholder.markdown(f'#### {full_response}', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
