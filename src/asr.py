import re
from num2words import num2words

special_char_replace = {
    "u\u0308": "ü",
    "a\u0308": "ä",
    "o\u0308": "ö",
    "\xa0": " ",
}

def normalize_sentence(
        sentence: str,
        language: str = 'de'
) -> str:
    """
        Normalize a sentence by lowercasing it, removing punctuation
        and replacing numbers with words.
    """

    # Replace special characters
    sentence = sentence.lower()
    for k, v in special_char_replace.items():
        sentence = sentence.replace(k, v)

    # Remove punctuation
    sentence = re.sub(r'[^\w\s]', '', sentence)

    for idx, word in enumerate(sentence.split()):
        if word.isnumeric():
            sentence[idx] = num2words(word, lang=language)

    return sentence


if __name__ == '__main__':
    sentence = "Hallo, wie geht's dir?"
    out = normalize_sentence(sentence)
    assert out == "hallo wie gehts dir"