import getpass
from constants.constants import SETTINGS_PATH
from utils.IO import read_json_file, write_json_file
from utils.utils import clear_terminal
from utils.terminalPrints import print_title, print_status
from utils.translations import get_translations
from utils.utils import get_settings

def change_language():
    settings = read_json_file(SETTINGS_PATH)
    current_language = settings.get("language", "es")
    new_language = "en" if current_language == "es" else "es"
    settings["language"] = new_language
    write_json_file(SETTINGS_PATH, settings)
    print(f"Language changed to {new_language}")

def settings_mode():
    while True:
        settings = get_settings()
        translations = get_translations()
        clear_terminal()
        print_title(translations["settings_mode_title"])
        index = 0

        # Print the topics selection
        for setting in settings["topics"]:
            index += 1
            print(f"{index}. {setting}: ", end="")
            print_status(settings["topics"][setting] == 1, translations["activated"], translations["desactivated"])

        # Print the language selection
        index += 1
        print(f"{index}. {translations['change_language']}: ", end="")
        print_status(settings.get("language", "es")=="en", translations["english_languaje"], translations["spanish_languaje"])

        # Print the exit and save option
        index += 1
        print(f"{index}. {translations['exit_and_save']}")
        
        # Check if the option is valid
        option = input("\n"+translations["option_prompt"])
        if (not option.isdigit() or int(option) < 1 or int(option) > index+2):
            print(translations["invalid_option_message"])
            getpass.getpass(translations["press_enter_message"])
            continue

        option = int(option)
        if option == index: # Exit and save
            break
        elif option == index-1: # Change language
            change_language()
            settings["language"] = "en" if settings["language"] == "es" else "es"  
        else: # Change the topic activation
            setting = list(settings["topics"].keys())[option-1]
            settings["topics"][setting] = abs(settings["topics"][setting] - 1)
            write_json_file(SETTINGS_PATH, settings)