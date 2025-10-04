import streamlit as st
import speech_recognition as sr
import pyttsx3
from openai import OpenAI
import threading
import time

# Page Configuration
st.set_page_config(
    page_title="TalkBot - A Virtual Voice Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Modern dark gradient background with particles effect */
    .main {
        padding: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%;
        animation: gradient 20s ease infinite;
        position: relative;
        overflow: hidden;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        25% { background-position: 50% 100%; }
        50% { background-position: 100% 50%; }
        75% { background-position: 50% 0%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Simple modern cursor trail */
    body {
        cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><circle cx="16" cy="16" r="8" fill="%2376b900" opacity="0.6"/><circle cx="16" cy="16" r="4" fill="%23ffffff"/></svg>') 16 16, auto;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 18px;
        padding: 14px;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 28px rgba(102, 126, 234, 0.6);
    }
    .stButton>button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }
    
    .chat-message {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        font-weight: 500;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .user-message {
        background: linear-gradient(135deg, rgba(30, 30, 30, 0.95), rgba(50, 50, 50, 0.95));
        border-left: 5px solid #667eea;
        color: #ffffff;
    }
    .ai-message {
        background: linear-gradient(135deg, rgba(20, 20, 20, 0.95), rgba(40, 40, 40, 0.95));
        border-left: 5px solid #f093fb;
        color: #ffffff;
    }
    
    .status-box {
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1rem 0;
        text-align: center;
        color: #000000;
        font-weight: 600;
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .listening {
        background: linear-gradient(135deg, rgba(255, 193, 7, 0.9), rgba(255, 152, 0, 0.9));
    }
    .success {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.9), rgba(56, 142, 60, 0.9));
        color: white;
    }
    .error {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.9), rgba(211, 47, 47, 0.9));
        color: white;
    }
    
    /* Style for sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));
        backdrop-filter: blur(20px);
    }
    
    /* Fix API key input visibility */
    .stTextInput>div>div>input[type="password"] {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #000000 !important;
        border-radius: 10px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        padding: 10px;
        font-size: 16px;
    }
    .stTextInput>div>div>input[type="password"]:focus {
        border-color: #667eea;
        box-shadow: 0 0 15px rgba(102, 126, 234, 0.3);
        background: rgba(255, 255, 255, 1) !important;
    }
    
    /* Stop button styling */
    div[data-testid="column"]:nth-child(3) .stButton>button {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%) !important;
        box-shadow: 0 8px 20px rgba(255, 65, 108, 0.4) !important;
    }
    div[data-testid="column"]:nth-child(3) .stButton>button:hover {
        background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%) !important;
        box-shadow: 0 12px 28px rgba(255, 65, 108, 0.6) !important;
    }
    
    /* Speaking indicator */
    .speaking-indicator {
        padding: 1rem;
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.9), rgba(56, 142, 60, 0.9));
        color: white;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        animation: pulse 1.5s ease-in-out infinite;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.02); }
    }
    
    /* Input field styling */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        padding: 10px;
        font-size: 16px;
        color: #000000;
    }
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 15px rgba(102, 126, 234, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "api_key" not in st.session_state:
    st.session_state.api_key = ""
if "tts_enabled" not in st.session_state:
    st.session_state.tts_enabled = True
if "is_speaking" not in st.session_state:
    st.session_state.is_speaking = False
if "stop_speaking" not in st.session_state:
    st.session_state.stop_speaking = False
if "tts_thread" not in st.session_state:
    st.session_state.tts_thread = None

# Speech Recognition
recognizer = sr.Recognizer()

# Global TTS engine reference
tts_engine = None

# Function to Speak AI Responses (runs in separate thread)
def speak_threaded(text):
    global tts_engine
    st.session_state.is_speaking = True
    st.session_state.stop_speaking = False
    
    try:
        # Initialize engine in this thread
        tts_engine = pyttsx3.init()
        tts_engine.setProperty("rate", 160)
        
        # Queue all text at once, then check periodically for stop signal
        tts_engine.say(text)
        
        # Start speaking in a way that allows interruption
        tts_engine.startLoop(False)
        
        # Keep the loop running and check for stop signal
        while tts_engine.isBusy():
            if st.session_state.stop_speaking:
                tts_engine.stop()
                break
            tts_engine.iterate()
            time.sleep(0.01)  # Small delay to prevent CPU overload
        
        tts_engine.endLoop()
        
        if tts_engine:
            try:
                del tts_engine
            except:
                pass
        tts_engine = None
        
    except Exception as e:
        print(f"TTS Error: {str(e)}")
        try:
            if tts_engine:
                tts_engine.stop()
        except:
            pass
    finally:
        st.session_state.is_speaking = False
        st.session_state.stop_speaking = False

def speak(text):
    if st.session_state.tts_enabled:
        # Start TTS in a separate thread
        thread = threading.Thread(target=speak_threaded, args=(text,), daemon=True)
        st.session_state.tts_thread = thread
        thread.start()

# Function to stop speaking
def stop_speech():
    st.session_state.stop_speaking = True
    global tts_engine
    if tts_engine:
        try:
            tts_engine.stop()
        except:
            pass
    # Wait a moment for the thread to finish
    time.sleep(0.3)
    st.session_state.is_speaking = False

# Function to Listen to Voice Input
def listen():
    with sr.Microphone() as source:
        status_placeholder.markdown('<div class="status-box listening">🎤 Listening... Please speak now!</div>', unsafe_allow_html=True)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            status_placeholder.markdown('<div class="status-box">🔄 Processing your speech...</div>', unsafe_allow_html=True)
            query = recognizer.recognize_google(audio)
            status_placeholder.markdown(f'<div class="status-box success">✅ Recognized: "{query}"</div>', unsafe_allow_html=True)
            return query
        except sr.WaitTimeoutError:
            status_placeholder.markdown('<div class="status-box error">⏱️ No speech detected. Please try again!</div>', unsafe_allow_html=True)
            return ""
        except sr.UnknownValueError:
            status_placeholder.markdown('<div class="status-box error">🤔 Could not understand audio. Please try again!</div>', unsafe_allow_html=True)
            return ""
        except sr.RequestError as e:
            status_placeholder.markdown(f'<div class="status-box error">❌ Speech service error: {str(e)}</div>', unsafe_allow_html=True)
            return ""

# Function to get AI response using NVIDIA API
def get_ai_response(question, api_key):
    try:
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )
        
        messages = []
        for msg in st.session_state.chat_history[-10:]:
            messages.append({"role": msg["role"], "content": msg["content"]})
        
        messages.append({"role": "user", "content": question})
        
        completion = client.chat.completions.create(
            model="meta/llama-3.1-405b-instruct",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )
        
        return completion.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("🤖 TalkBot")
    st.markdown("### *A Virtual Voice Assistant*")

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    api_key_input = st.text_input(
        "Paste Your API Key",
        type="password",
        value=st.session_state.api_key,
        help="Paste your API key"
    )
    
    if api_key_input:
        st.session_state.api_key = api_key_input
        st.success("✅ API Key loaded!")
    else:
        st.warning("⚠️ Please paste your API key")
    
    st.markdown("---")
    
    st.session_state.tts_enabled = st.toggle("🔊 Enable Text-to-Speech", value=st.session_state.tts_enabled)
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📝 How to Use")
    st.markdown("""
    1. Paste your API key above
    2. Click 'Start Listening' or type
    3. Ask your question
    4. Use 🛑 Stop to interrupt AI
    """)

# Main content area
status_placeholder = st.empty()

# Speaking indicator
if st.session_state.is_speaking:
    st.markdown('<div class="speaking-indicator">🔊 AI is speaking... Click Stop to interrupt</div>', unsafe_allow_html=True)

# Input methods
col1, col2, col3 = st.columns([1.2, 1.2, 0.6])

with col1:
    if st.button("🎤 Start Listening", disabled=not st.session_state.api_key or st.session_state.is_speaking):
        if not st.session_state.api_key:
            st.error("Please paste your API key in the sidebar!")
        else:
            user_query = listen()
            if user_query:
                with st.spinner("🤔 AI is thinking..."):
                    ai_response = get_ai_response(user_query, st.session_state.api_key)
                
                st.session_state.chat_history.append({"role": "user", "content": user_query})
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                
                speak(ai_response)
                status_placeholder.empty()
                st.rerun()

with col2:
    text_input = st.text_input("💬 Or type your message:", key="text_input", disabled=st.session_state.is_speaking)
    if st.button("📤 Send", disabled=not st.session_state.api_key or st.session_state.is_speaking or not text_input):
        if text_input and st.session_state.api_key:
            with st.spinner("🤔 AI is thinking..."):
                ai_response = get_ai_response(text_input, st.session_state.api_key)
            
            st.session_state.chat_history.append({"role": "user", "content": text_input})
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            
            speak(ai_response)
            st.rerun()

with col3:
    if st.button("🛑 Stop", disabled=not st.session_state.is_speaking, key="stop_btn"):
        stop_speech()
        st.rerun()

# Display Chat History
st.markdown("---")
st.subheader("💬 Chat History")

if st.session_state.chat_history:
    # Reverse the chat history to show newest first
    for idx in range(len(st.session_state.chat_history) - 1, -1, -1):
        msg = st.session_state.chat_history[idx]
        if msg["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>👤 You:</strong><br>
                    {msg["content"]}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message ai-message">
                    <strong>🤖 AI Assistant:</strong><br>
                    {msg["content"]}
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("👋 No messages yet. Start a conversation by speaking or typing!")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: white; padding: 1rem; font-weight: 600; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
        <p>🚀 TalkBot - A Virtual Voice Assistant | Built with Streamlit</p>
    </div>
""", unsafe_allow_html=True)