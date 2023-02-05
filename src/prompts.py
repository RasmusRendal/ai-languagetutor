import openai
from utils import strip, merge_evaluations

def sentence_is_correct(original, translation):
    prompt = "Say YES if \"" + translation + "\" is a correct translation of \"" + original + "\" into German. If the translation is wrong, explain why.\nAnswer:"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.3,
      max_tokens=100
    )
    answer = response.choices[0].text
    return answer

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
      prompt="This is the evaluation of a German learner's grammar abillities, from a scale from 1 to 5, 1 being best and 5 being worst. Adjust the scores based on a sentence the user has just translated. If you do not know a user's abillities in a specific category, leave it unchanged.\nBegin evaluation: " + skills + "\nBegin sentence:\n" + sentence + "\nBegin new evaluation:\n",
      max_tokens=len(skills)+10,
      temperature=0.3
    )
    # TODO: Check that skills are adjusted correctly
    return strip(merge_evaluations(skills, response.choices[0].text))

def one_exercise(skills):
    sentence = generate_exercise(skills);
    print("Translate the following sentence into German:")
    print(sentence)
    translation = input("> ")
    is_correct = sentence_is_correct(sentence, translation)
    if "YES" in is_correct.upper():
        print("Sentence correctly translated. Generating another one.")
    else:
        print(is_correct)
    skills = adjust_skills(skills, translation)
    return skills


