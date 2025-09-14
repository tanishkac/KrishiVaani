from llm.translation_engine import Translator

# Create a single translator instance when the module loads
translator = Translator()

def handle_farmer_query(mistral_answer: str, detected_lang: str) -> str:
    """
    Take the English output from Mistral and, if required,
    translate it to the farmer's detected language.
    """
    if detected_lang == "en":
        return mistral_answer
    return translator.translate(mistral_answer, target_lang=detected_lang)
