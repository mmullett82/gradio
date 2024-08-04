import openai
import gradio
import streamlit as st
import subprocess

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an expert in the assistance of guiding people to a better solution."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-4o",
        messages = messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "chaiT")

# Run the Gradio interface in a separate subprocess
gradio_app_script = 'chaiT.py'

# Run the gradio app script
process = subprocess.Popen(['python', gradio_app_script])

# Embed the Gradio app in Streamlit using an iframe
st.markdown(
    """
    <iframe src="http://localhost:7860/" width="100%" height="600"></iframe>
    """,
    unsafe_allow_html=True
)

# Keep Streamlit running
st.write("The Gradio app should be displayed above.")

demo.launch(share=True)