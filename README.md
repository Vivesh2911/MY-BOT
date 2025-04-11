
# Simple Voice Chatbot with Speech-to-Text and Text-to-Speech

This is a simple voice-based chatbot built using Python. It allows users to interact with the bot through speech. The bot can respond to user input with speech, including telling jokes and providing weather updates.

### Features:
- **Speech-to-Text**: The bot listens to your voice and converts it into text.
- **Text-to-Speech**: The bot responds with speech, making it more interactive.
- **Chatbot Features**:
  - Tells jokes.
  - Provides weather-related information.
  - Ends the conversation when the user says "bye".

### Requirements

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `random`

### Installation

1. **Clone the repository** (or download the zip):
   ```bash
   git clone https://github.com/your-username/voice-chatbot.git
   ```

2. **Install the required dependencies**:

   Install the required Python libraries using `pip`:
   ```bash
   pip install SpeechRecognition pyttsx3
   ```

   You might also need to install additional libraries for `speech_recognition` to work properly. On macOS, for example, you can install `portaudio` (if you haven't done so yet):
   ```bash
   brew install portaudio
   ```

3. **Run the script**:
   After installing the dependencies, run the script with:
   ```bash
   python my_bot.py
   ```

### Usage

- When you run the bot, it will listen for your voice input.
- You can ask the bot to:
  - Tell a **joke**: "Tell me a joke."
  - Provide **weather** tips: "What's the weather like?"
  - End the conversation: "Bye."
- The bot will respond with speech.

### Example Interaction

```
Bot: Hello! I am your friendly bot. How can I help you today?
You: Tell me a joke.
Bot: Why don’t skeletons fight each other? They don’t have the guts.
You: What's the weather like?
Bot: It looks like it might rain, better take an umbrella.
You: Bye.
Bot: Goodbye! Have a great day.
```

### How It Works

- **Speech-to-Text**: The bot listens to your speech and converts it into text using the `speech_recognition` library.
- **Text-to-Speech**: The bot responds with speech using the `pyttsx3` library.
- **Commands**: The bot can respond to specific commands, such as telling a joke or giving weather advice, based on the keywords it detects.

### Troubleshooting

- If you encounter any issues with the speech recognition, make sure the microphone permissions are enabled on your device.
- If you get errors with `pyttsx3`, make sure the appropriate text-to-speech engines are installed.

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

