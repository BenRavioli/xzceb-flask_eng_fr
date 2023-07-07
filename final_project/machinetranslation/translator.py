"""
Translates from French to English and vice versa
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)

    return french_text


def french_to_english(french_text):
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)

    return english_text
