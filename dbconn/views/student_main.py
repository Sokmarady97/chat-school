from flask import Blueprint, render_template, request, jsonify, redirect

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

