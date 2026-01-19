#!/usr/bin/env python3

"""
Test script to verify that the personal AI assistant works on Linux
"""

import sys
import os

# Add the current directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported"""
    try:
        from core.speech import recognize_wake_word
        from core.commands import execute_commands
        from core.ai import ask_gemini
        from core.history import log_history
        from utils.tts import speak
        from utils.system_control import shutdown_pc, restart_pc, sleep_pc
        from utils.app_control import open_application, close_application
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_tts():
    """Test text-to-speech functionality"""
    try:
        from utils.tts import speak
        speak("Text to speech is working correctly on Linux")
        print("✓ Text-to-speech test completed")
        return True
    except Exception as e:
        print(f"✗ Text-to-speech test failed: {e}")
        return False

def test_config():
    """Test that config file can be read"""
    try:
        from config import WAKE_WORD, GENAI_API_KEY
        print(f"✓ Config loaded - Wake word: {WAKE_WORD}")
        return True
    except Exception as e:
        print(f"✗ Config test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Linux compatibility for Personal AI Assistant...")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_tts
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Tests completed: {passed}/{len(tests)} passed")
    if passed == len(tests):
        print("🎉 All tests passed! The assistant should work correctly on Linux.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")