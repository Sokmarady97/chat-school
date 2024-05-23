from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/Chatup")
def chatup_page():
    return render_template("./Chat_Up_Call.html")

if __name__ == "__main__":
    app.run(debug=True)