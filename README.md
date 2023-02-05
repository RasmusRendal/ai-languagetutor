# AI Language Tutor
Built on OpenAI, this program prompts you to translate sentences into German, correcting you when you're wrong, and trying to match your level.
As it stands, this is merely a POC.

## Usage:
To use it, you need an API key from [OpenAI](https://platform.openai.com/).
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
The teacher asked the students to write an essay about their summer vacation.
> Die Lehrer bete die Studenten um einen Essay zu schreiben über ihres Sommerurlaub
 No, the translation is wrong. The correct translation is "Der Lehrer bat die Studenten, einen Aufsatz über ihren Sommerurlaub zu schreiben."

ARTICLE_USE changed from 5 to 3
VERB_CONJUGATION changed from 5 to 3
WORD_ORDER changed from 5 to 3
PUNCTUATION changed from 5 to 4
SPELLING changed from 5 to 4
CAPITALIZATION changed from 5 to 4
TENSES changed from 5 to 3
PREPOSITIONS changed from 5 to 4
SUBJECT_VERB_AGREEMENT changed from 5 to 3
DIRECT_OBJECT changed from 5 to 3
INDIRECT_OBJECT changed from 5 to 3
INFINITIVES changed from 5 to 3
GERUNDS changed from 5 to 3
NOMINATIVE_CASE changed from 5 to 3
ACCUSATIVE_CASE changed from 5 to 3
DATIVE_CASE changed from 5 to 3
GENITIVE_CASE changed from 5 to 3

Translate the following sentence into German:
The boy is playing with his toys.
```
