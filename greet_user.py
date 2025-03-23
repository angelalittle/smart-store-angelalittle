"""
greet_user.py - A simple Python script that demonstrates user interaction and text-to-speech.

Date: January 2025
"""

#####################################
# Imports At the Top
#####################################

# Import from external dependencies (must be installed)
# See requirements.txt 
import pyttsx3

# Import from local project modules
from utils_logger import logger

#####################################
# Define Helper Functions
#####################################

def speak_message(message: str) -> None:
    """
    Speak the given message using text-to-speech.

    Args:
        message (str): The text to speak out loud.
    """
    try:
        engine = pyttsx3.init()  # Initialize the text-to-speech engine
        engine.say(message)  # Queue the message to be spoken
        engine.runAndWait()  # Wait for the speech to complete
    except Exception as e:
        logger.error(f"Error with text-to-speech: {e}")

#####################################
# Define main Function
#####################################

def main() -> None:
    """
    Main function to greet the user in multiple languages and read it out loud.
    """
    logger.info("Starting main function.")

    # Get the user's name
    user_name: str = input("Enter your name to continue: ")

    # Create a greeting message in multiple languages
    greetings = [
        f"Hello, {user_name}! Welcome to Python programming.",  # English
        f"Hola, {user_name}! Bienvenido a la programación en Python.",  # Spanish
        f"你好, {user_name}! 欢迎学习Python编程.",  # Chinese (Mandarin)
        f"Bonjour, {user_name}! Bienvenue à la programmation Python.",  # French
        f"Hallo, {user_name}! Willkommen bei der Python-Programmierung.",  # German
        f"హలో, {user_name}! Python ప్రోగ్రామింగ్‌లోకి స్వాగతం.",  # Telugu
        f"Hei, {user_name}! Velkommen til Python-programmering.",  # Norwegian
    ]

    # Add a user confirmation at the start
    caution_message = "Caution: This program can speak. Do you want to hear the greetings? (Y/N): "

    # Ask the user if they want to proceed
    response = input(caution_message).strip().lower()

    # Print and speak each greeting
    for greeting in greetings:
        logger.info(greeting)
        if response == 'y':
            speak_message(greeting)

    logger.info("Exiting main function.")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    logger.info("HELLO - Ready for work.")
    main()
    logger.info("HELLO - Execution complete.")
