from prompts import *
from is_correct import answer_to_bool, sentence_is_correct

class MistakenSentence:
    def __init__(self, original, translation):
        self.original = original
        self.translation = translation
        self.goodness = 8

    def generate_exercise(self):
        return self.original

    def __str__(self):
        return "Sentence \"" + self.original + "\" with ease " + str(self.goodness)


class GrammarStructure:
    def __init__(self, name):
        self.name = name
        self.goodness = 2

    def generate_exercise(self):
        pass


class System:
    def __init__(self):
        self.iteration = 1
        self.schedule = {}
        self.languagetool = False


    def add_to_schedule(self, obj):
        new_index = self.iteration + obj.goodness
        while new_index in self.schedule:
            new_index += 1
        self.schedule[new_index] = obj


    def do_iteration(self):
        if self.iteration in self.schedule:
            obj = self.schedule[self.iteration]
            sentence = obj.generate_exercise()
            print("Translate the following sentence into German:")
            print(sentence)
            translation = input("> ")
            is_correct = sentence_is_correct(sentence, translation, languagetool=self.languagetool)
            if answer_to_bool(is_correct):
                print("Sentence correctly translated! Good job!")
                obj.goodness *= 2
            else:
                print(is_correct)
                obj.goodness = 2
            self.add_to_schedule(obj)
        else:
            sentence = generate_generic_exercise()
            print("Translate the following sentence into German:")
            print(sentence)
            translation = input("> ")
            is_correct = sentence_is_correct(sentence, translation, languagetool=self.languagetool)
            if answer_to_bool(is_correct):
                print("Sentence correctly translated! Good Job!")
            else:
                print(is_correct)
                self.add_to_schedule(MistakenSentence(sentence, translation))
        self.iteration += 1


