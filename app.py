# app.py
from flask import Flask, request, render_template, session, redirect, url_for
from variables import (questions_seller, questions_seller_a, questions_seller_b, questions_seller_c, 
                       questions_buyer, questions_car, questions_transaction, documento)
from transform_answers import transform_document
from create_pdf import create_pdf

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Establece una clave secreta para la sesión

@app.route('/', methods=['GET', 'POST'])
def index():
    session['responses'] = {}  # Inicializar o reiniciar las respuestas almacenadas
    session.modified = True
    print("Respuestas reiniciadas")  # Depuración
    return redirect(url_for('question', question_id=0))  # Empezar con la primera pregunta

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    all_questions = questions_seller + questions_seller_a + questions_seller_b + questions_seller_c + questions_buyer + questions_car + questions_transaction

    print(f"Actual question_id: {question_id}")  # Depuración

    if question_id >= len(all_questions):
        print("Todas las preguntas han sido respondidas")  # Depuración
        return redirect(url_for('generate_document'))

    current_question = all_questions[question_id]
    print(f"Mostrando pregunta: {current_question}")  # Depuración

    if request.method == 'POST':
        answer = request.form.get('answer')
        session['responses'][current_question] = answer
        session.modified = True
        print(f"Respuesta guardada: {answer}")  # Depuración

        next_question_id = question_id + 1
        if next_question_id < len(all_questions):
            return redirect(url_for('question', question_id=next_question_id))

        return redirect(url_for('generate_document'))

    return render_template('question.html', question=current_question, question_id=question_id)

@app.route('/generate_document')
def generate_document():
    print("Generando documento con las respuestas")  # Depuración
    documento_final = transform_document(session['responses'], documento)
    output_pdf = "output.pdf"
    create_pdf(documento_final, output_pdf)
    return render_template('success.html', pdf_file=output_pdf)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')