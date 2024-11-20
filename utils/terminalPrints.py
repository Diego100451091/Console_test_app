from constants.constants import COLORS, BG_COLORS
from utils.translations import get_translations

def print_title (title: str = ""):
    """
    Print a title in purple color

    Args:
        title (str): Title to print
    """
    print(
            f"{COLORS['purple']}===============| {title} |==============={COLORS['reset']}")

def print_colored_text(text: str = "", color: str = "reset", end="\n"):
    """
    Print a text with the specified color

    Args:
        text (str): Text to print
        color (str): Color to use
        end (str): End character to use
    """

    if color in COLORS.keys():
        print(f"{COLORS[color]}{text}{COLORS['reset']}", end=end)
    else:
        print(text)

def print_text_with_bg(text: str = "", color: str = "reset", end="\n"):
    """
    Print a text with the specified background color
    
    Args:
        text (str): Text to print
        color (str): Background color to use
        end (str): End character to use
    """
    if color in BG_COLORS.keys():
        print(f"{BG_COLORS[color]}{text}{COLORS['reset']}", end=end)
    else:
        print(text)

def print_progress(status_vector: list):
    """
    Print a progress bar with the status vector

    Args:
        status_vector (list): List of status to print. Possible values are:
            0: Not started
            1: Success
            -1: Error
    """
    print(get_translations()["progress_message"], end="")
    current_done = 0
    for status in status_vector:
        if status == 0:
            print("■", end="")
        elif status == 1:
            print_colored_text("■", "green", end="")
            current_done += 1
        elif status == -1:
            print_colored_text("■", "red", end="")
            current_done += 1
    print(f" {current_done}/{len(status_vector)}\n")

def print_question(question: str = "", options: list = []):
    """
    Print a question with the specified options
    
    Args:
        question (str): Question to print
        options (list): List of options to print
    """
    translations = get_translations()
    print(translations["question_title"], question)
    print(translations["options_title"])
    for i in range(len(options)):
        print("\t", chr(97+i) + ".", options[i])

def print_status(active: bool, activatedString: str ="Activated", desactivatedString: str ="Desactivated"):
    """
    Print a status with the specified strings

    Args:
        active (bool): Status to print
        activatedString (str): String to print if the status is active
        desactivatedString (str): String to print if the status is desactivated
    """
    if (active):
        print_text_with_bg(activatedString, "cyan", end="  ")
        print(desactivatedString)
    else:
        print(activatedString, end="  ")
        print_text_with_bg(desactivatedString, "cyan")