# 🤖 TalkBot - Virtual Voice Assistant

<div align="center">

**An intelligent voice-powered chatbot with speech recognition and text-to-speech capabilities**

**Python 3.8+ | Streamlit 1.31.0 | OpenAI API | MIT License**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

<table>
<tr>
<td>

### 🎤 **Voice Recognition**
- Real-time speech-to-text conversion
- Ambient noise adjustment
- Multiple language support via Google Speech API

</td>
<td>

### 🔊 **Text-to-Speech**
- Natural voice responses
- Adjustable speech rate
- Interruptible playback

</td>
</tr>
<tr>
<td>

### 💬 **Smart Conversations**
- Context-aware responses
- Powered by Meta's Llama 3.1 405B
- Chat history retention

</td>
<td>

### 🎨 **Beautiful UI**
- Modern gradient design
- Responsive layout

</td>
</tr>
</table>

---

## 🎥 Demo

### Voice Interaction
```
User: 🎤 "What's the weather like today?"
TalkBot: 🤖 "I can help you with that! However, I don't have..."
```

### Text Chat
```
User: 💬 "Tell me a joke"
TalkBot: 🤖 "Why did the programmer quit his job? Because he..."
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Microphone (for voice input)
- Speakers/Headphones (for voice output)
- API Key 

### Step 1: Clone the Repository

```bash
git clone https://github.com/Weird-ragazzo/TalkBot---Simple-Voice-Assistant
cd TalkBot---Simple-Voice-Assistant
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Install PyAudio (Platform Specific)

#### Windows
```bash
pip install pyaudio
```

#### macOS
```bash
brew install portaudio
pip install pyaudio
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

---

## 💻 Usage

### Quick Start

1. **Run the application:**
   ```bash
   streamlit run TalkBot-API.py
   ```

2. **Open your browser** at `http://localhost:8501`

3. **Enter your API key** in the sidebar

4. **Start chatting!** Choose voice or text input

### Voice Commands

- Click **"🎤 Start Listening"** to speak
- Speak clearly into your microphone
- Wait for the AI response
- Click **"🛑 Stop"** to interrupt speech

### Text Input

- Type your message in the text box
- Click **"📤 Send"** to submit
- View responses in the chat history

---

## ⚙️ Configuration

### API Key Setup

1. Get your API key
2. Paste it in the sidebar of the application
3. The key is stored in your session (not saved permanently)

### Customization

#### Change AI Model
Edit the model in `TalkBot-API.py`:
```python
model="meta/llama-3.1-405b-instruct"  # Change this
```

#### Adjust Speech Rate
Modify TTS speed:
```python
tts_engine.setProperty("rate", 160)  # Default: 160 (increase/decrease)
```

#### Change Theme Colors
Edit the CSS gradient in the code:
```python
background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, ...);
```

---

## 📦 Project Structure

```
talkbot/
│
├── TalkBot-API.py          # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation

```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **SpeechRecognition** | Voice-to-text conversion |
| **pyttsx3** | Text-to-speech engine |
| **OpenAI SDK** | API integration for AI model |
| **NVIDIA API** | Llama 3.1 405B model access |
| **Threading** | Asynchronous TTS processing |

---

## 🎯 Features Breakdown

### Speech Recognition
- ✅ Real-time audio capture
- ✅ Ambient noise filtering
- ✅ Google Speech API integration
- ✅ Timeout and error handling
- ✅ Visual feedback during listening

### Text-to-Speech
- ✅ Natural voice synthesis
- ✅ Background threading
- ✅ Interruptible playback
- ✅ Customizable speech rate
- ✅ Cross-platform compatibility

### AI Integration
- ✅ Context-aware conversations
- ✅ Chat history management (last 10 messages)
- ✅ Streaming responses
- ✅ Error handling
- ✅ Temperature control for creativity

### User Interface
- ✅ Modern gradient design
- ✅ Animated backgrounds
- ✅ Responsive layout
- ✅ Dark theme optimized
- ✅ Status indicators
- ✅ Chat history display

---

## 🐛 Troubleshooting

### Microphone Not Working

**Issue:** "No speech detected" error

**Solutions:**
- Check microphone permissions
- Ensure microphone is set as default input device
- Try adjusting ambient noise duration:
  ```python
  recognizer.adjust_for_ambient_noise(source, duration=2)  # Increase duration
  ```

### PyAudio Installation Error

**Issue:** `Failed building wheel for pyaudio`

**Solutions:**
- **Windows:** Download prebuilt wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- **macOS:** Install portaudio first: `brew install portaudio`
- **Linux:** Install dev packages: `sudo apt-get install portaudio19-dev`

### TTS Not Working

**Issue:** No audio output from text-to-speech

**Solutions:**
- Check system audio settings
- Verify pyttsx3 installation: `pip install --upgrade pyttsx3`
- Try disabling and re-enabling TTS in sidebar

### API Key Error

**Issue:** "Invalid API key" or connection errors

**Solutions:**
- Verify your NVIDIA API key is correct
- Check internet connection
- Ensure API quota hasn't been exceeded
- Try generating a new API key

---

## 🤝 Contributing

Contributions are welcome!

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include type hints where applicable
- Test your changes thoroughly
- Update documentation as needed
  
---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Streamlit** for the amazing web framework
- **OpenAI** for the SDK
- **Google** for Speech Recognition API
- All contributors and users of TalkBot


---

### ⭐ If you like this project, please give it a star!

Made with ❤️ by Dhruv Raghav(https://github.com/Weird-ragazzo)


</div>

---

<div align="center">

**[⬆ Back to Top](#-talkbot---virtual-voice-assistant)**

</div>
