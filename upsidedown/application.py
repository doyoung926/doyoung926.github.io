from flask import Flask, render_template, request, redirect, url_for
import sys
application = Flask(__name__)
from io import StringIO
import io


@application.route("/")
def main():
    return render_template("main.html")

@application.route("/result")
def result():
    change_word = request.args.get("change_word")
    word_count = len(change_word)

    def return_print():
        io = StringIO()

        for i in range(1, word_count + 1, 1):
            print(change_word[-i], file=io, end="")

        return io.getvalue()

    result = return_print()
    print(result)
    
    return render_template("result.html", result = result) 
    
if __name__ == "__main__":
    application.run(host='0.0.0.0')