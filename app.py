import streamlit as st
import time
import logging
from model_pipeline import train_fake_news_model, predict_news_veracity

# --- SILENCE INTERNAL THREAD WARNINGS ---
streamlit_logger = logging.getLogger("streamlit.runtime.scriptrunner_utils.script_run_context")
streamlit_logger.setLevel(logging.ERROR)

# Set professional layout configurations
st.set_page_config(
    page_title="AI Fake News Detector",
    page_icon="📰",
    layout="centered"
)

# --- App Header Interface ---
st.title("📰 AI-Powered Fake News Detector")
st.markdown(
    "This intelligent portal screens public headlines and articles against "
    "historical textual markers using an optimized **Passive-Aggressive Machine Learning Classifier** pipeline."
)
st.write("---")

# --- Model Loading Section (Cached for High Speed) ---
@st.cache_resource
def load_and_train_system():
    vectorizer, model = train_fake_news_model()
    return vectorizer, model

with st.spinner("🧠 Bootstrapping AI Brain Engine & analyzing 45,000 articles... Please wait."):
    start_time = time.time()
    vectorizer, model = load_and_train_system()
    elapsed = round(time.time() - start_time, 2)

st.toast(f"Machine Learning Model fully loaded in {elapsed}s!", icon="🚀")

# --- User Input Field Section ---
st.subheader("🔮 Analyze Unseen Content Veracity")
user_input = st.text_area(
    "Paste the news headline or complete article text body below:",
    placeholder="Type or paste suspected clickbait, broadcast transcripts, or social claims here...",
    height=150
)

# --- Evaluation Core Routine ---
if st.button("Verify Content Authenticity", type="primary"):
    if not user_input.strip():
        st.warning("⚠️ Input prompt is completely empty. Please enter text to run the verification engine.")
    else:
        with st.spinner("🕵️‍♂️ Running semantic syntax analysis..."):
            verdict = predict_news_veracity(user_input, vectorizer, model)
            time.sleep(0.4) 
            
        st.write("### Assessment Result:")
        
        if verdict == "FAKE":
            st.error("🚨 **PROBABLE FALSEHOOD DETECTED**")
            st.markdown(
                f"> **Classification Verdict:** This content aligns heavily with common text structures, "
                f"sensationalized language, or vocabulary markers historically flagged as **{verdict}**."
            )
        else:
            st.success("🟢 **AUTHENTIC / TRUE NEWS STRUCTURE**")
            st.markdown(
                f"> **Classification Verdict:** This content shows standard structural reporting attributes, "
                f"aligning cleanly with records historically cataloged as **{verdict}**."
            )
            
        col1, col2 = st.columns(2)
        col1.metric(label="System Verdict", value=verdict)
        col2.metric(label="Model Status", value="Active / Operational")