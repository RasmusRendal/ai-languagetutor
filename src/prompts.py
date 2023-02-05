import openai
from utils import strip, merge_evaluations, has_decreases

def answer_to_bool(answer):
    return "YES" in answer.upper() or "JA" in answer.upper()

def sentence_is_correct(original, translation):
    prompt = "Verify whether the following German sentence is gramatically correct:\nSentence: " + translation + "\nAnswer:"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.1,
      max_tokens=100
    )
    answer = strip(response.choices[0].text)
    if not answer_to_bool(answer):
        return answer


    prompt2 = "Is \"" + translation + "\" a correct translation of \"" + original + "\" into German?"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt2,
        temperature=0,
        max_tokens=100)
    return strip(response.choices[0].text)


def generate_generic_exercise():
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Generate a simple English sentence, that the user can translate into German for grammar practice.",
      temperature=0.6,
      max_tokens=40)
    return strip(response.choices[0].text)


def generate_exercise_with_structure():
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="Generate a simple English sentence, that the user can translate into German for grammar practice.",
      temperature=0.6,
      max_tokens=40)
    return strip(response.choices[0].text)



def generate_exercise(skills):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="You are to act as a German grammar tutor. You generate sentences in English the user is to translate to German. Please generate a sentence for a user with abillities, described from 1-5 with 1 being best and 5 being worst, where you try to focus on one area the user is bad at. The skills of the user are the following:\n Begin user evaluation" + skills + "\n End user evaluation. Begin English sentence: ",
      temperature=0.6,
      max_tokens=40
    )
    return strip(response.choices[0].text)

def adjust_skills(skills, sentence):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="This is the evaluation of a German learner's grammar abillities, from a scale from 1 to 5, 1 being best and 5 being worst. Print new scores for 3 of these categories, based on a sentence the user has written. The scores should get worse if a user made a relevant mistake, and better if the user used the grammar correctly.\nBegin evaluation: " + skills + "\nBegin sentence:\n" + sentence + "\nBegin changed scores:\n",
      max_tokens=40,
      temperature=0.3
    )
    return strip(response.choices[0].text)

def one_exercise(skills):
    sentence = generate_exercise(skills);
    print("Translate the following sentence into German:")
    print(sentence)
    translation = input("> ")
    is_correct = sentence_is_correct(sentence, translation)
    adjusted_skills = adjust_skills(skills, translation)
    if "YES" in is_correct.upper() and not has_decreases(skills, adjusted_skills):
        print("Sentence correctly translated. Generating another one.")
    elif "YES" in is_correct.upper():
        print("Your sentence was somehow wrong, but the language model did detect why.")
    else:
        print(is_correct)
    skills = merge_evaluations(skills, adjusted_skills)
    return skills


