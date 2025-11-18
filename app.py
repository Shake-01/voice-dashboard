import streamlit as st
import speech_recognition as sr

st.title("🎤 Voice Notepad")

#session state to store transcribe
if "notes" not in st.session_state:
  st.session_state.notes = ""

#create a recognizer
recognizer = sr.Recognizer()

#button to record audio
if st.button("Start Recording"):
  with sr.Micrphone() as source:
    st.write("Listening...")
    audio = recognizer.listen(source)

  try: 
    text = recognizer.recognize_google(audio)
    st.session_state.notes += text + "/n"
    st.success(f"Recorded: {text}")

  except:
    st.error("Sorry, I couldn't understand.")

#display notes
st.text_area("Your Notes:", st.session_state.notes, height=300)
    
