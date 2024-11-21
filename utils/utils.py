import os
import random
from utils.IO import read_json_file
from constants.constants import QUESTIONS_PATH, SETTINGS_PATH, WRONG_QUESTIONS_PATH
from utils.translations import get_translations

def clear_terminal():
    """
    Clears the terminal screen.

    This function checks the operating system and clears the terminal screen accordingly.
    On Windows, it uses the 'cls' command to clear the screen, while on Unix-based systems
    it uses the 'clear' command.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_exit():
    """
    Asks the user for input to either continue or exit the program.

    Returns:
    - True if the user inputs 'exit'
    - False if the user inputs anything else
    """
    translations = get_translations()
    text = input("\n"+translations["press_enter_or_continue_message"]+"\n")
    if text == "exit":
        return True
    else:
        return False

def get_settings():
    themes = read_json_file(QUESTIONS_PATH).keys()
    # Set the settings with the themes as keys and 1 as value
    settingsSchema = {
        "topics": {theme: 1 for theme in themes},
        "language": "es"
    }
        
    previous_settings = read_json_file(SETTINGS_PATH)
    if (read_json_file(SETTINGS_PATH) != None):
        settings = previous_settings
        for key in settingsSchema:
            if key not in previous_settings:
                settings[key] = settingsSchema[key]
    else:
        settings = settingsSchema
    return settings


def get_questions():
    settings = get_settings()
    questions = []
    all_questions = read_json_file(QUESTIONS_PATH)
    for setting in settings["topics"]:
        if (settings["topics"][setting] == 1):
            # Add the list to the questions list
            questions += all_questions[setting]
    return questions

def get_wrong_questions():
    data = read_json_file(WRONG_QUESTIONS_PATH)
    return data if data else []

def randomize_options(options, answer):
    randomized_options = list(options.values())
    random.shuffle(randomized_options)
    correct_option = ["a", "b", "c", "d"].pop(randomized_options.index(answer))
    return randomized_options, correct_option