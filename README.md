# Personal AI Assistant - Linux Version

This is a Linux-compatible version of the Personal AI Assistant. The assistant has been modified to work with Linux systems, including Kali Linux.

**For detailed setup and usage instructions, please refer to the full documentation below.**

## Features

- Voice-controlled AI assistant
- Wake word detection ("bro")
- Text-to-speech responses
- AI-powered responses using Google Gemini
- System control (shutdown, restart, sleep)
- Application management (open, close, minimize, maximize)
- Web search capabilities
- History tracking
- PDF export of AI responses

## Prerequisites

- Python 3.8 or higher
- Virtual environment support
- Audio input device (microphone)
- Audio output device (speakers/headphones)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd personal-AI-assistant
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the assistant using the provided shell script:
```bash
./run_assistant.sh
```

Or run directly with Python:
```bash
source venv/bin/activate
python main.py
```

## Voice Commands

- Say "bro" to activate the assistant
- "Open [application]" - Opens the specified application
- "Close [application]" - Closes the specified application
- "Search on chrome [query]" - Searches for the query on Google Chrome
- "Shutdown" - Shuts down the system
- "Restart" - Restarts the system
- "Sleep" - Puts the system to sleep
- "Current time" - Gets the current time
- "Date" - Gets the current date
- "Ask [question]" - Ask any question to the AI
- "Show my history" - Shows command history (requires password)
- "Clear history" - Clears command history (requires password)
- "Download" or "Save response" - Saves the last AI response as a PDF
- "Bye" - Stops the assistant

## Linux-Specific Modifications

The following changes have been made to make the assistant compatible with Linux:

1. **System Control Commands**: 
   - Windows `shutdown` commands replaced with Linux equivalents
   - Uses `systemctl suspend` for sleep mode

2. **Application Management**:
   - Windows-specific application handling replaced with Linux-compatible methods
   - Application name mapping for common Linux applications
   - Uses `pkill` for closing applications

3. **Window Management**:
   - Uses `xdotool` for window minimize/maximize operations (if available)

4. **Dependencies**:
   - Removed Windows-specific packages (`pywin32`)
   - Kept cross-platform packages

## Configuration

The assistant can be configured through `config.py`:
- `WAKE_WORD`: The word to activate the assistant (default: "bro")
- `VOICE_PASSWORD`: Password for sensitive operations (default: "008")
- `GENAI_API_KEY`: Google Gemini API key for AI functionality

## Troubleshooting

### No Audio Input
Ensure your microphone is properly connected and configured in your system settings.

### Application Control Issues
Some applications might not respond to open/close commands. This can happen if:
1. The application name doesn't match the expected Linux command
2. The application is not installed on your system
3. Window management tools like `xdotool` are not installed (for minimize/maximize)

To install xdotool on Debian/Ubuntu-based systems:
```bash
sudo apt install xdotool
```

### Missing Dependencies
If you encounter import errors, make sure you've activated the virtual environment and installed all dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.