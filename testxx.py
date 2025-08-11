import streamlit as st
import openai
import streamlit as st
from dotenv import load_dotenv
import openai
from dotenv import load_dotenv
import os
from datetime import date
load_dotenv()
client = openai.OpenAI (
# Set the base URL and key for Groq
    api_key = os.getenv("OPENROUTER_API_KEY"),
    base_url = "https://openrouter.ai/api/v1"
)

def news_app(topic):
    
    
    prompt = f"""
    You are an expert news anchor.

    Here is a topic:
    {topic}

        search the internet for the latest news updates as on {date.today()} on the given topic and provide the key points of the
        news feed without fabricating any news and just report reliable data. Also provide the reference links from
        which you have looked up the news content.
    """

    try:
        response = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct",
    messages=[
        
        {"role": "user", "content": prompt}
    ]
)
        final_output =  response.choices[0].message.content
        
        return final_output
    except Exception as e:
        return f"⚠️ Error from local model: {e}"
# ---------- Streamlit UI ----------


''' Module to display news'''
st.title("🤖 AI News display")
st.subheader("Enter the topic you are interested in")

topic = st.text_area("🧾 Enter the topic")

if topic:
    with st.spinner("Analyzing topic..."):
        if st.button("🔁 Display the news headlines"):
                   
            output_news = news_app(topic)
            st.markdown(output_news)