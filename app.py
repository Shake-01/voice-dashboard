import streamlit as st
from st_audio_recorder import st_audio_recorder
import speech_recognition as sr
import tempfile

st.title("🎤 Voice Notepad (Streamlit Cloud Compatible)")

# Session state for notes
if "notes" not in st.session_state:
    st.session_state.notes = ""

st.write("Click below and speak:")

# Record audio through browser
audio_data = st_audio_recorder()

# If the user recorded audio
if audio_data is not None:
    st.success("Audio recorded!")

    # Save audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_data)
        audio_file_path = f.name

    # Transcribe using SpeechRecognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.session_state.notes += text + "\n"
        st.write(f"**Transcribed:** {text}")

    except Exception as e:
        st.error("Could not transcribe audio.")

# Show notes
st.text_area("📝 Your Notes:", st.session_state.notes, height=300)

