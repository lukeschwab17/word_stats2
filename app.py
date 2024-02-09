from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/word", methods=["POST"])
def word_stats():
    word = request.form.get("word")
    # if bad input, fail
    if not word or (not word.replace(' ', '').isalpha()):
        return render_template("fail.html")

    words = word.split(" ")
    word_count = len(words)
    char_count = len(word)
    avg_word_length = 0
    for word in words:
        avg_word_length += len(word)
    avg_word_length /= word_count
    return render_template("success.html", word=word, word_count=word_count, char_count=char_count, avg_word_length=avg_word_length)
