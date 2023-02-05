# AI Language Tutor
Built on OpenAI, this program prompts you to translate sentences into German, correcting you when you're wrong, and trying to match your level.
As it stands, this is merely a POC.

## Usage:
To use it, you need an API key from [OpenAI](https://platform.openai.com/) (A free account gets you 18$ worth of content, which lets you run this program for a long time).
Set the environment variable `OPENAI_API_KEY` to your key, and run `./src/main.py`.
You should get something like the following interaction:
```
# ./src/main.py
Initial evaluation:
ARTICLE_USE=5
VERB_CONJUGATION=5
WORD_ORDER=5
PUNCTUATION=5
SPELLING=5
CAPITALIZATION=5
TENSES=5
MODAL_VERBS=5
SEPARABLE_VERBS=5
INSEPARABLE_VERBS=5
PREPOSITIONS=5
ADVERBS=5
ADJECTIVES=5
NEGATIVE_FORMULATION=5
PASSIVE_VOICE=5
SUBJECT_VERB_AGREEMENT=5
DIRECT_OBJECT=5
INDIRECT_OBJECT=5
INFINITIVES=5
GERUNDS=5
NOMINATIVE_CASE=5
ACCUSATIVE_CASE=5
DATIVE_CASE=5
GENITIVE_CASE=5
POSSESSIVE_PRONOUNS=5
RELATIVE_PRONOUNS=5
CONJUNCTIONS=5
INTERJECTIONS=5

Translate the following sentence into German:
The teacher gave the students a difficult test.
> Der Lehrer gab die Studenten eine schwere Prüfung
Sentence correctly translated. Generating another one.

ARTICLE_USE changed from 5 to 1
VERB_CONJUGATION changed from 5 to 1
WORD_ORDER changed from 5 to 1
PUNCTUATION changed from 5 to 1
SPELLING changed from 5 to 1

Translate the following sentence into German:
"The students should have written the exam yesterday."
> Die Studenten sollen die Exam gestern geschreiben hat
 No, the translation is wrong. The correct translation is "Die Studenten sollten gestern die Prüfung schreiben."

ARTICLE_USE changed from 4 to 5
VERB_CONJUGATION changed from 4 to 5
WORD_ORDER changed from 4 to 5
PUNCTUATION changed from 2 to 5
SPELLING changed from 3 to 5
```

## Current state
`davinci` is naturally not always completely correct about grammar.
There's bound to be false positives and false negatives.
Additionally, when adjusting its evaluation of the users abilities, it is way to overeager.
