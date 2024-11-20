import random
from utils.utils import clear_terminal, get_exit
from utils.terminalPrints import print_title, print_progress, print_question
from utils.utils import get_questions
from utils.translations import get_translations

def study_mode():
    tranlations = get_translations()
    remaining_questions = get_questions()

    status_vector = []
    total_dictionary_lenght = len(remaining_questions)
    for i in range(total_dictionary_lenght):
        status_vector.append(0)
    status_index = 0

    while True:
        clear_terminal()
        print_title(tranlations["study_mode_title"])

        print_progress(status_vector)
        
        if (len(remaining_questions) == 0):

            print(tranlations["all_questions_shown_message"])
            break

        question = remaining_questions.pop(random.randrange(len(remaining_questions)))
        print_question(question["question"], list(question["options"].values()))
        print(tranlations["response_prompt"], question["answer"])

        status_vector[status_index] = 1
        status_index += 1
        
        if get_exit():
            break

