from flask import Flask, render_template, request
from summary import Summary

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def summarize():
    summ = Summary()
    _text = request.form['paragraph']
    summary = summ.run(_text)
    return (summary)

if __name__ == "__main__":
    app.run()



