"""
Instgram_Like_Robot (Ver.1)
Created by MJ. Liu
2021/10/21
"""

from flask import Flask, request, render_template
from script import run_script

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/process", methods=["POST"])
def process():
    account = request.form.get("account")
    password = request.form.get("password")
    run_script(account,password)
    return render_template("success.html")

if __name__ == "__main__":
    app.run()
