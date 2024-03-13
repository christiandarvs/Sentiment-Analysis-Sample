import streamlit as st
from textblob import TextBlob


def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Classify the polarity as positive, negative, or neutral
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"


def clear_text():
    st.session_state["text"] = ""


st.header("Sentiment Analysis")
text = st.text_input("Enter text: ", key="text")

if st.button("Analyze", type="secondary"):
    result = analyze_sentiment(text)
    st.button("Clear", on_click=clear_text)
    st.write(
        f"Result: {result}",
    )
