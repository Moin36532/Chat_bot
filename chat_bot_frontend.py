# Taking imports
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage,BaseMessage
from dotenv import load_dotenv 
from chat_bot_backend import graph_chatbot
# CODE:


#defining thread id for memory purpose:
thread_id = 1
config = {'configurable':{'thread_id':thread_id}}

# Showing previous messages on screen:
if "messages" not in st.session_state:
    st.session_state['messages'] = []
for msg in st.session_state['messages']:
    with st.chat_message(msg["role"],avatar=msg["avatar"]):
        st.text(msg["content"])



# Taking user input:
user_input = st.chat_input("Enter here:")
if user_input:
    #update the session state to include the new message
    st.session_state['messages'].append({"role":"user","content":user_input,"avatar": "🧑"})
    with st.chat_message("user",avatar="🧑"):
        st.text(user_input)
    #invoke the backend model here:
    with st.chat_message("assistant",avatar="🤖"):
# Doing streaming so that response appears word by word:
        ai_message = st.write_stream(
            data.content for data,meta_data in graph_chatbot.stream(
            {'messages':HumanMessage(content=user_input)},
            config=config,
            stream_mode = 'messages'
            ))
        #update the session state to include the AI message:
        st.session_state['messages'].append({"role":"assistant","content":ai_message,"avatar": "🤖"})


