from flask import Flask,request

app = Flask(__name__)
import json

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/parse2/<text>',methods=["POST","GET"])
def parser2(text):
    sentence = text
    return json.dumps(parse(sentence))


@app.route('/parse/',methods=["POST","GET"])
def parser():
    if request.method == "GET":
        sentence = request.args.get('key', '')
        return json.dumps(parse(sentence))

    if request.method == "POST":
        sentence = request.form['key']
        print(sentence)
        return json.dumps(parse(sentence))

from nltk import tag,tokenize
from nltk.stem import WordNetLemmatizer

def parse(sentence):
    wordnet_lemmatizer = WordNetLemmatizer()

    pre_tokens = tokenize.word_tokenize(sentence.lower())
    tokens = [wordnet_lemmatizer.lemmatize(pre_token) for pre_token in pre_tokens]

    print(tokens)

    tags = tag.pos_tag(tokens)
    print(tags)

    return_set = [{tag[0]:tag[1][0]} for tag in tags if tag[1][0] in ['N','V','J','I','C','R']]
    print(return_set)

    return return_set


if __name__ == '__main__':
    print(parse("I love you."))
    app.run(host="0.0.0.0",port=8000)
