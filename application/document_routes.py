from flask import request, jsonify, render_template
from flask_login import login_required
from .question_manager import QuestionnaireManager

@app.route('/create_document', methods=['GET', 'POST'])
@login_required
def create_document():
    questionnaire = QuestionnaireManager(session)
    if 'questions' not in session:
        questionnaire.initialize()
        questionnaire.fetch_questions(session['current_question_set'])

    if request.method == 'POST':
        # Call logic to save response and advance question index
        save_response_and_advance(request.form['response'])  
        return jsonify({'success': True})

    current_questions = session.get('questions', [])
    question_index = session.get('question_index', 0)

    if current_questions:
        current_question = current_questions[question_index]
        set_name = session.get('current_set_name', 'Set de Preguntas')
        full_question_label = f"{set_name}: Pregunta {question_index + 1}"
        return render_template('questions.html',
                               question=current_question,
                               question_label=full_question_label,
                               question_index=question_index,
                               text=text)