# Voice Assistant in Python 🗣️💻

This is a simple voice assistant built using Python. It listens to your voice commands and can perform basic tasks like telling the time, date, searching the web, and having a simple conversation.

## 🚀 Features

- Greet the user and respond to "hello"
- Tell the current time and date
- Search Google based on voice input
- Respond to unrecognized commands
- Exit gracefully with voice command like "bye" or "exit"

## 🛠️ Technologies Used

- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pyaudio](https://pypi.org/project/PyAudio/)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [webbrowser](https://docs.python.org/3/library/webbrowser.html)

## 🖥️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/voice-assistant.git
    cd voice-assistant
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    If you don't have `PyAudio` installed, install it via:
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```

3. **Run the script**:
    ```bash
    python assistant.py
    ```

## 🧠 How It Works

- The assistant uses the `speech_recognition` library to listen to the user's voice via the microphone.
- Recognized voice input is parsed and checked for specific keywords.
- Based on the command, the assistant can respond using `pyttsx3` for text-to-speech or open a Google search.
- It will keep running until the user says "exit" or "bye".

## 📝 Example Commands

- `hello`
- `what is the time`
- `what is today's date`
- `search artificial intelligence`
- `exit`

## 📌 Requirements

- Python 3.x
- Microphone
- Internet connection (for Google Speech Recognition and web search)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize and enhance this assistant to include more features like weather updates, reminders, or integration with external APIs!

