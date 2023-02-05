import openai
from languagetool import languagetool_check
from utils import strip

def answer_to_bool(answer):
    return "YES" in answer.upper() or "JA" in answer.upper()

def grammatically_correct(sentence, languagetool=False):
    if languagetool_check(sentence):
        prompt = "Verify whether the following German sentence is gramatically correct:\nSentence: " + sentence + "\nAnswer:"
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0.1,
          max_tokens=100
        )
        return strip(response.choices[0].text)
    else:
        prompt = "Why is the following German sentence grammatically incorrect?\nSentence: " + sentence + "\nAnswer:"
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0.1,
          max_tokens=100
        )
        return strip(response.choices[0].text)


def sentence_is_correct(original, translation, languagetool=False):
    grammar = grammatically_correct(translation, languagetool=languagetool)
    if not answer_to_bool(grammar):
        return grammar

    prompt2 = "Is \"" + translation + "\" a correct translation of \"" + original + "\" into German?"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt2,
        temperature=0,
        max_tokens=100)
    return strip(response.choices[0].text)

