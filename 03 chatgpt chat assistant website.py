import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an expert in the assistance of guiding people to a better solution."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-4o",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "chaiT")

demo.launch(share=True)
