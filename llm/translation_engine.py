# nlu/translation_engine.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translator:
    def __init__(self, model_name="facebook/m2m100_418M"):
        """
        Load a multilingual translation model.
        This supports en <-> hi, en <-> or, etc.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate(self, text: str, target_lang: str) -> str:
        """
        Translate from English to target_lang.
        target_lang: "hi" (Hindi), "or" (Odia), "en" (English), etc.
        """
        # Mistral output is in English, so source is English
        self.tokenizer.src_lang = "en"
        encoded = self.tokenizer(text, return_tensors="pt")

        generated_tokens = self.model.generate(
            **encoded,
            forced_bos_token_id=self.tokenizer.get_lang_id(target_lang)
        )

        return self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
