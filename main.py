import getpass

from utils.IO import read_json_file, delete_file
from utils.utils import clear_terminal
from utils.terminalPrints import print_title
from utils.translations import get_translations
from components.studyMode import study_mode
from components.guessMode import guess_mode
from components.settings import settings_mode, get_settings

def main():
    while True:
        translations = get_translations()

        clear_terminal()
        print_title(translations["menu_title"])
        print(translations["select_mode_introduction"])
        print(f"1. {translations['select_mode_study']}")
        print(f"2. {translations['select_mode_test']}")
        print(f"3. {translations['select_mode_error']}")
        print(f"4. {translations['select_mode_delete_error']}")
        print(f"5. {translations['select_mode_settings']}")
        print(f"6. {translations['select_mode_exit']}")
        option = input("\n"+translations["option_prompt"])
        if option == "1":
            study_mode()
        elif option == "2":
            guess_mode()
        elif option == "3":
            wrong_dict = read_json_file("wrong_questions.json")
            if wrong_dict:
                guess_mode(wrong_dict)
            else:
                print(translations["no_wrong_questions_message"])
                getpass.getpass(translations["press_enter_message"])
        elif option == "4":
            delete_file("wrong_questions.json")
            print(translations["delete_record_message"])
            getpass.getpass(translations["press_enter_message"])
        elif option == "5":
            settings_mode()
        elif option == "6":
            break
        else:
            print(translations["invalid_option_message"])
            getpass.getpass(translations["press_enter_message"])

if __name__ == "__main__":
    main()
