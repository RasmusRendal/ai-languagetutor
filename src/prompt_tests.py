from is_correct import sentence_is_correct, answer_to_bool
from languagetool import start_server
"""Use this file to tweak the prompts"""

def is_correct(original, translation):
    res = sentence_is_correct(original, translation)
    print(res)
    return answer_to_bool(res)

assert start_server()

assert is_correct("The dog is running in the park.", "Der Hund läuft im Park")
assert is_correct("The sun is shining brightly.", "Die Sonne scheint hell.")
# Could be correct in a fragment >_>
# Therefore, nobody can detect it
#assert not is_correct("The sun is shining brightly.", "Der Sonne scheint hell.")
assert not is_correct("The cat is sleeping on the bed.", "Der Katze schlaft auf dem Bett.")
assert not is_correct("The sky is blue", "Die Himmel ist blau.")
