from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/Chatup")
def Chat_Up_Call():
    return render_template("Chat_Up_Call.html")

@app.route("/Mainpage")
def Main():
    return render_template("Main_page.html")

@app.route("/StudentQuestionPage")
def Question():
    return render_template("Student_question_board_detail.html")

@app.route("/QuestionPage")
def QuestionPage():
    return render_template("전문1.html")

if __name__ == "__main__":
    app.run(debug=True)