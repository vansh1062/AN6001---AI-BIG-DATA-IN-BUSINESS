from flask import Flask # type: ignore
from flask import render_template,request
import textblob as tb
import google.generativeai as genAI  # type: ignore
import os

api = os.getenv("makersuite")
genAI.configure(api_key = "api")
model = genAI.GenerativeModel("gemini-1.5-flash-002")

app = Flask("__name__")

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA", methods=["GET", "POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result", methods=["GET", "POST"])
def SA_result():
    q = request.form.get("q")
    r = tb.TextBlob(q).sentiment
    return(render_template("SA_result.html", r=r))

@app.route("/genAI", methods=["GET", "POST"])
def genAI():
    return(render_template("genAI.html"))

@app.route("/genAI_result", methods=["GET", "POST"])
def genAI_result():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("genAI_result.html", r=r.candidate[0].content.parts[0].text))

if __name__ == "__main__":
    app.run()