from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

user_score = 0
computer_score = 0

@app.route("/")
def portfolio():
    return render_template("portfolio.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    global user_score, computer_score

    result = ""
    computer_choice = ""
    winner = None

    if request.method == "POST":

        if request.form.get("restart") == "yes":
            user_score = 0
            computer_score = 0
            return redirect(url_for("game"))

        user_choice = request.form["choice"]
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You Win!"
            user_score += 1
        else:
            result = "Computer Wins!"
            computer_score += 1

        # 🎯 Check if someone reached 5
        if user_score == 5:
            winner = "You"
            user_score = 0
            computer_score = 0

        elif computer_score == 5:
            winner = "Computer"
            user_score = 0
            computer_score = 0

    return render_template("index.html",
                           result=result,
                           computer_choice=computer_choice,
                           user_score=user_score,
                           computer_score=computer_score,
                           winner=winner)

if __name__ == "__main__":
    app.run(debug=True)
