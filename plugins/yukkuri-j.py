from slackbot.bot import listen_to
import subprocess
import urllib
import re
import jctconv


#C0ZJ755FV


def Kanji2Hiragana(message):
    text = re.sub(':.*:', '', message)
    text = re.sub('\n', '', text)
    p1 = subprocess.Popen(['echo', text], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['mecab', '-Oyomi'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    return jctconv.kata2hira(re.sub(r'\n', '', output.decode('utf-8')))


@listen_to("")
def default_func(message):
    channel = message.body["channel"]
    if channel == "C0ZJ755FV":
        text = message.body["text"]
        text = Kanji2Hiragana(text)
        if text == "ゆっくりしていってね":
            text = '"' + text + '"'
            print(text)
            subprocess.run(["saykana", "-s", "50", text])
        else:
            text = '"' + text + '"'
            print(text)
            subprocess.run(["saykana", text])