from flask import Blueprint, render_template, request, jsonify, redirect, Flask
bp = Blueprint('student_main', __name__, url_prefix='/student')



@bp.route('/')
def chat_up_call():
    return render_template('./Student_page/Chat_Up_Call_page/Chat_Up_Call.html')


@bp.route('/main')
def main():
    return render_template('./Student_page/Main_page/Main_page.html')


@bp.route('/question')
def question():
    return render_template('./Student_page/Student_question_board_detail/Student_question_board_detail.html')


@bp.route('/comment')
def comment():
    return render_template('./Student_page/Student_question_board_detail/전문1.html')


@bp.route('/submit')
def submit():
    return render_template('./Student_page/Chatbot_choice_page/chatbot_choice_page.html')


@bp.route('/submit_doc_to_chatbot')
def submit_doc_to_chatbot():
    return render_template('Student_page/Chatbot_Or_Communication_Page/Chatbot_or_communication_page.html')
