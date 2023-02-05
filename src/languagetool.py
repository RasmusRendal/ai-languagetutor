import requests
import subprocess
import time

def languagetool_check(sentence):
    r = requests.post("http://127.0.0.1:8081/v2/check", data={"text": sentence, "language": "de-AT", "picky": True}).json()
    return len(r['matches']) == 0

def start_server():
    try:
        subprocess.Popen(["languagetool-http-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        time.sleep(5)
        return True
    except:
        return False

