import sys
import random
import getpass
from utils.utils import clear_terminal
from utils.terminalPrints import print_title, print_progress, print_colored_text, print_question
from utils.IO import read_json_file, write_json_file, append_json_file
from utils.utils import get_questions, get_wrong_questions, get_exit, randomize_options, are_explanations_enabled
from utils.translations import get_translations
from constants.constants import WRONG_QUESTIONS_PATH

def guess_mode():
    questions = get_questions()
    _guess_mode(questions)

def guess_wrong_questions_mode():
    translations = get_translations()

    wrong_questions = get_wrong_questions()
    if len(wrong_questions) == 0:
        print(translations["no_wrong_questions_message"])
        getpass.getpass(translations["press_enter_message"])
        return 
        
    _guess_mode(wrong_questions)

def _guess_mode(questions):
    translations = get_translations()

    # Reset the wrong questions file
    write_json_file(WRONG_QUESTIONS_PATH, [])

    questions = questions
    wrong_questions = []
    
    status_vector = []
    total_questions_lenght = len(questions)
    for i in range(total_questions_lenght):
        status_vector.append(0)
    status_index = 0

    while True:
        clear_terminal()
        print_title(translations["test_mode_title"])
        print_progress(status_vector)

        if (len(questions) == 0):
            print(translations["all_questions_shown_message"])
            break

        question = questions.pop(random.randrange(len(questions)))
        randomized_options, correct_option = randomize_options(question["options"], question["options"][question["answer"]])
       
        print_question(question["question"], randomized_options)

        user_answer = get_user_answer()

        if (user_answer == correct_option):
            print_colored_text(translations["correct_message"], "green")
            status_vector[status_index] = 1
        else:
            print_colored_text(translations["incorrect_message"], "red", "")
            print(translations["correct_option_message"], correct_option)
            if question.get("explanation") and are_explanations_enabled():
                print(translations["explanation_message"], question["explanation"])
            status_vector[status_index] = -1
            wrong_questions.append(question)
            append_json_file(WRONG_QUESTIONS_PATH, question)

        status_index += 1

        if get_exit():
            break

    show_wrong_questions(wrong_questions)

def get_user_answer():
    while True:
        answer = input("_\r")
        if (answer in ["a", "b", "c", "d"]):
            return answer
        # Go one line up and remove the line
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()


def show_wrong_questions(wrong_questions):
    translations = get_translations()
    print("\n"+translations["wrong_questions_paragraph"])
    for question in wrong_questions:
        print_question(question["question"], list(question["options"].values()))
        print(translations["response_prompt"], question["answer"],"\n")

    get_exit()

