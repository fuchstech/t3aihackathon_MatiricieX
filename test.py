from flask import Flask, jsonify, request

app = Flask(__name__)

# Soru bankası
test_questions = [
    {
        'id': 1,
        'question': 'Hangi hormon kan şekerini düzenler?',
        'options': ['Adrenalin', 'İnsülin', 'Kortizol', 'Tiroksin'],
        'correct': 'İnsülin'
    },
    {
        'id': 2,
        'question': 'İnsan vücudunda kaç kemik vardır?',
        'options': ['206', '210', '180', '220'],
        'correct': '206'
    }
    # Ek sorular buraya eklenebilir...
]

# Soru almak için API
@app.route('/get_question', methods=['GET'])
def get_question():
    question_id = int(request.args.get('id', 1))
    question = next((q for q in test_questions if q['id'] == question_id), None)
    return jsonify(question)

# Cevap kontrolü için API
@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_id = data['id']
    user_answer = data['answer']
    question = next((q for q in test_questions if q['id'] == question_id), None)

    if question and user_answer == question['correct']:
        return jsonify({'result': 'correct'})
    else:
        return jsonify({'result': 'incorrect'})

if __name__ == '__main__':
    app.run(debug=True)
