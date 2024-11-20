from utils.IO import read_json_file
from constants.constants import SETTINGS_PATH

def load_translations(language):
    translations = read_json_file(f'translations/{language}.json')
    return translations[language] if translations else None

def get_translations():
    settings = read_json_file(SETTINGS_PATH)
    language = settings.get("language", "es")
    translations = load_translations(language)
    return translations