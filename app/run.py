# init.py
from vernam import *
from flask import Flask, render_template, jsonify, request
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Answers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# models.py


class Question(db.Model):
    __tablename__ = "Question"
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_string = db.Column(db.String(200))
    answer1_string = db.Column(db.String(200))
    answer2_string = db.Column(db.String(200))
    answer3_string = db.Column(db.String(200))
    answer4_string = db.Column(db.String(200))
    correct_answer = db.Column(db.String)

    def __init__(self, question_string, answer1_string, answer2_string, answer3_string, answer4_string, correct_answer):
        self.question_string = question_string
        self.answer1_string = answer1_string
        self.answer2_string = answer2_string
        self.answer3_string = answer3_string
        self.answer4_string = answer4_string
        self.correct_answer = correct_answer

    def checkAns(self, answer):
        if (self.correct_answer == answer):
            return 1
        return 0


def getquestion(id):
    db.create_all()
    q = Question.query.filter_by(question_id=id).first()
    temp = {}
    temp['question'] = q.question_string
    temp['answer1_string'] = q.answer1_string
    temp['answer2_string'] = q.answer1_string
    temp['answer3_string'] = q.answer1_string
    temp['answer4_string'] = q.answer1_string
    temp['correct_answer'] = q.correct_answer
    return temp


# routes.py


@app.route('/')
@app.route('/Introduction')
def Introduction():
    return render_template('Introduction.html')


@app.route('/Theory')
def Theory():
    return render_template('Theory.html')


@app.route('/Procedure')
def Procedure():
    return render_template('Procedure.html')


@app.route('/Objective')
def Objective():
    return render_template('Objective.html')


@app.route('/Experiment')
def Experiment():
    return render_template('Experiment.html')


@app.route('/Further')
def Further():
    return render_template('Further.html')


@app.route('/Assignment')
def Assignment():
    return render_template('Assignment.html')


@app.route('/Feedback')
def Feedback():
    return render_template('Feedback.html')


@app.route('/Experiment/next_plain_text', methods=['GET'])
def nextplaintext():
    info = {
        "plainarea": Vernam_RandSequence(PLAIN_TEXT_LEN)
    }
    return jsonify(info)


@app.route('/Experiment/next_key', methods=['GET'])
def nextkey():
    key_len = random.randint(6, 12)
    info = {
        "key": Vernam_RandSequence(key_len)
    }
    return jsonify(info)


@app.route('/Experiment/Next_Encryption', methods=['GET'])
def Next_Encryption():
    info = {
        "current_encryption": Vernam_RandSequence(PLAIN_TEXT_LEN)
    }
    return jsonify(info)


@app.route('/Experiment/Encrypt1', methods=['POST'])
def Encrypt1():
    data = request.get_json()
    plaintext = str(data.get('plainarea'))
    key = str(data.get('key'))
    current_encryption = str(data.get('current_encryption'))
    info = {
        "ciphertext": encrypt(plaintext, key, current_encryption)
    }
    return jsonify(info)

# we enter the user_key; so there is a possibilty of the user entering an invalid input; in this case do
@app.route('/Experiment/gen_all_pairs', methods=['POST'])
def gen_all_pairs():
    data = request.get_json()
    message = ""
    encryption_set = ""
    user_key = str(data.get('user_key'))
    current_encryption = str(data.get('current_encryption'))
    if(valid_binary_str(user_key) == 0):
        message = "Entered string is not a valid binary string. Enter a valid string as the user key"
    elif (len(user_key) < 1):
        message = "Enter some binary string as the user key"
    else:
        encryption_set = generate_all_pairs(user_key, current_encryption)
    info = {
        "encryption_set": encryption_set,
        "message": message
    }
    return jsonify(info)


@app.route('/Experiment/checkAnswer', methods=['POST'])
def check_answer():
    data = request.get_json()
    message = ""
    results = ""
    messageType = ""
    user_key = str(data.get('user_key'))
    current_encryption = str(data.get('current_encryption'))
    m1 = str(data.get('m1'))
    m2 = str(data.get('m2'))
    yesno = str(data.get('yesno'))
    if(valid_binary_str(user_key) == 0):
        message = "Entered string for the user key is not valid. Enter a valid binary string"
        messageType = "user_key"
    elif (len(user_key) < 1):
        message = "Enter a binary string as the user key"
        messageType = "user_key"
    if(yesno == "yes"):
        message = ""
        results = "This is not correct, Please try again!"
    else:
        if(valid_binary_str(m1) == 0):
            message = "Entered string for m1 is not valid. Enter a valid binary string"
            messageType = "m1"
        elif (len(m1) < 1):
            message = "Enter a binary string as m1"
            messageType = "m1"
        elif(valid_binary_str(m2) == 0):
            message = "Entered string for m2 is not valid. Enter a valid binary string"
            messageType = "m2"
        elif (len(m2) < 1):
            message = "Enter a binary string as m2"
            messageType = "m2"
        elif(m1 == m2):
            message = "Enter different strings for m1 and m2"
            messageType = "m12"
        else:
            results = checkAnswer(yesno, m1, m2, user_key, current_encryption)
    info = {
        "results": results,
        "message": message,
        "messageType": messageType
    }
    return jsonify(info)


@app.route('/Experiment/simulation_key_generator', methods=['POST'])
def simulation_key_generator():
    data = request.get_json()
    message = ""
    messageType = ""
    key = ""
    plaintext = str(data.get('simulation_plainarea'))
    ciphertext = str(data.get('simulation_cipherarea'))
    if(valid_binary_str(plaintext) == 0):
        message = "Entered string for plaintext is not valid. Enter a valid binary string"
        messageType = "plaintext"
    elif(valid_binary_str(ciphertext) == 0):
        message = "Entered string for ciphertext is not valid. Enter a valid binary string"
        messageType = "ciphertext"
    else:
        key = simulation_key_gen(plaintext, ciphertext)
    info = {
        "simulation_key": key,
        "message": message,
        "messageType": messageType
    }
    return jsonify(info)


@app.route('/Experiment/simulation_encrypt', methods=['POST'])
def simulation_encrypt():
    message = ""
    messageType = ""
    ciphertext = ""
    data = request.get_json()
    plaintext = str(data.get('simulation_plainarea'))
    key = str(data.get('simulation_key'))
    if(valid_binary_str(plaintext) == 0):
        message = "Entered string for plaintext is not valid. Enter a valid binary string"
        messageType = "plaintext"
    elif(len(plaintext) == 0):
        message = "Enter a binary string as plaintext for encryption"
        messageType = "plaintext"
    elif(valid_binary_str(key) == 0):
        message = "Entered string for key is not valid. Enter a valid binary string with p=0.5"
        messageType = "key"
    elif(check_key(key) == 0):
        message = "Entered string for key is not valid. p should be 0.5"
        messageType = "key"
    elif (len(key) < len(plaintext)):
        message = "Key must be atleast the length of the Plaintext"
        messageType = "key"
    else:
        ciphertext = simencrypt(plaintext, key)
    info = {
        "simulation_cipherarea": ciphertext,
        "message": message,
        "messageType": messageType
    }
    return jsonify(info)


@app.route('/Experiment/simulation_decrypt', methods=['POST'])
def simulation_decrypt():
    data = request.get_json()
    message = ""
    messageType = ""
    ciphertext = str(data.get('simulation_cipherarea'))
    key = str(data.get('simulation_key'))
    plaintext = ""
    if(valid_binary_str(key) == 0):
        message = "Entered string for key is not valid. Enter a valid binary string with p=0.5"
        messageType = "key"
    elif(check_key(key) == 0):
        message = "Entered string for key is not valid. p should be 0.5"
        messageType = "key"
    elif(valid_binary_str(ciphertext) == 0):
        message = "Entered string for ciphertext is not valid. Enter a valid binary string"
        messageType = "ciphertext"
    elif(len(ciphertext) == 0):
        message = "Enter a binary string as ciphertext for encryption"
        messageType = "ciphertext"
    elif (len(key) < len(ciphertext)):
        message = "Key must be atleast the length of the ciphertext"
        messageType = "key"
    else:
        plaintext = simdecrypt(ciphertext, key)
    info = {
        "message": message,
        "messageType": messageType,
        "simulation_plainarea": plaintext
    }
    return jsonify(info)


@app.route('/Quizzes')
def Quizzes():
    return render_template('Quizzes.html')


@app.route('/Quizzes/getQuestions', methods=['GET'])
def getQ():
    questions = dict()
    rand = random.sample(range(1, 10), 5)
    q = Question.query.filter_by(question_id=rand[0]).first()
    questions['question_1'] = q.question_string
    questions['answer1_string_1'] = q.answer1_string
    questions['answer2_string_1'] = q.answer2_string
    questions['answer3_string_1'] = q.answer3_string
    questions['answer4_string_1'] = q.answer4_string
    questions['QID1'] = q.question_id
    q = Question.query.filter_by(question_id=rand[1]).first()
    questions['question_2'] = q.question_string
    questions['answer2_string_2'] = q.answer2_string
    questions['answer3_string_2'] = q.answer3_string
    questions['answer4_string_2'] = q.answer4_string
    questions['QID2'] = q.question_id
    questions['answer1_string_2'] = q.answer1_string
    q = Question.query.filter_by(question_id=rand[2]).first()
    questions['question_3'] = q.question_string
    questions['answer1_string_3'] = q.answer1_string
    questions['answer2_string_3'] = q.answer2_string
    questions['answer3_string_3'] = q.answer3_string
    questions['answer4_string_3'] = q.answer4_string
    questions['QID3'] = q.question_id
    q = Question.query.filter_by(question_id=rand[3]).first()
    questions['question_4'] = q.question_string
    questions['answer1_string_4'] = q.answer1_string
    questions['answer2_string_4'] = q.answer2_string
    questions['answer3_string_4'] = q.answer3_string
    questions['answer4_string_4'] = q.answer4_string
    questions['QID4'] = q.question_id
    q = Question.query.filter_by(question_id=rand[4]).first()
    questions['question_5'] = q.question_string
    questions['answer1_string_5'] = q.answer1_string
    questions['answer2_string_5'] = q.answer2_string
    questions['answer3_string_5'] = q.answer3_string
    questions['answer4_string_5'] = q.answer4_string
    questions['QID5'] = q.question_id
    return jsonify(questions)


@app.route('/Quizzes/Evaluate', methods=['POST'])
def Eval():
    data = request.get_json()
    score = 0
    temp = dict()
    temp['Correct'] = ""
    qid = int(data['QID1'])
    ans = data['answer_1']
    q = Question.query.filter_by(question_id=qid).first()
    if(q.correct_answer == ans):
        score += 1
        temp['Correct'] += "1 "

    qid = data['QID2']
    ans = data['answer_2']
    q = Question.query.filter_by(question_id=qid).first()
    if(q.checkAns(ans) == 1):
        score += 1
        temp['Correct'] += "2 "

    qid = data['QID3']
    ans = data['answer_3']
    q = Question.query.filter_by(question_id=qid).first()
    if(q.checkAns(ans) == 1):
        score += 1
        temp['Correct'] += "3 "

    qid = data['QID4']
    ans = data['answer_4']
    q = Question.query.filter_by(question_id=qid).first()
    if(q.checkAns(ans) == 1):
        score += 1
        temp['Correct'] += "4 "

    qid = data['QID5']
    ans = data['answer_5']
    q = Question.query.filter_by(question_id=qid).first()
    if(q.checkAns(ans) == 1):
        score += 1
        temp['Correct'] += "5 "
    temp['Correct'] = 'Questions answered correct: ' + temp['Correct']
    temp['Score'] = 'Your score: '+str(score * 20)+'%'
    return jsonify(temp)


def FillQuestionDatabase():
    #Number of questions : 9
    db.create_all()
    question_string = "Using Vernam cipher, a ciphertext can be decrypted to a statement and its opposite. Mark the appropriate comment:"
    answer1_string = "Silly statement"
    answer2_string = "No! A Vernam ciphertext can be interpreted to different plaintext messages but they all mean the same thing."
    answer3_string = "Indeed"
    answer4_string = "Not so, a Vernam cipher may decrypt to the plaintext that generated it and to a large number of pseudo-random statements, but not to a statement and its opposite."
    correct_answer = "1"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)

    question_string = " In a stream cipher a seed is multiplied and transposed many time with itself to generate an infinite randomized output. Mark the appropriate comment: "
    answer1_string = "Not multiplied -- added to itself, then transposed."
    answer2_string = "No, the seed shifts the bits from one register to the next, then shifts them back, and forward again and again to generate the infinite randomized sequence"
    answer3_string = "No, the seed is copied to the bin registers, then it is changed every round as a result of XOR operation between the bits in the registers, then the bits are being right-shifted and the rightmost bits is pushed out to join the long randomized sequence "
    answer4_string = "Pretty accurate, well put."
    correct_answer = "2"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)
    question_string = "Stream ciphers are almost as unbreakable as a Vernam cipher because, almost all the bits of the seeds are XORed with the key. Mark the appropriate comment: "
    answer1_string = "just about right "
    answer2_string = "true only for shift registers. "
    answer3_string = "Stream cipher used with a perfectly randomized seed is as unbreakable as Vernam. "
    answer4_string = "In some stream ciphers XOR operations are used between bits in the registers, but the algorithm is based on a small seed, which can be hacked."
    correct_answer = "3"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)
    question_string = "A random sequence is a sequence where one always follows zero, and zero always follows one. Mark the appropriate comment: "
    answer1_string = "True indeed. "
    answer2_string = "Only true for sequences extracted from quantum radiation. "
    answer3_string = "No, a random sequence is one where there are exactly the same number of ones and zeros "
    answer4_string = "In a long enough random sequence in about half of the cases 1 follows 1 and half of the cases 0 follows 1."
    correct_answer = "4"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)

    question_string = "In a block cipher the plaintext is chopped into blocks, and each block is encrypted with its own key, so that if one block is cracked the other survive. Mark the correct statement below: "
    answer1_string = "Wrong! In a block cipher the first block is XOR-ed with the key, and the result is XOR-ed with the next block!"
    answer2_string = "Not so. A block cipher is a stream cipher where the contents is well divided into blocks like columns in a database. "
    answer3_string = "Very much so."
    answer4_string = "Not really, a block-cipher key is re-used for successive blocks. "
    correct_answer = "3"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)

    question_string = "Choose the correct ciphertext obtained after encrypting the plaintext 0100 0011 0111 using the key 0111 0110 1010"
    answer1_string = "0011 0101 1101"
    answer2_string = "0101 1101 0001"
    answer3_string = "0011 1101 0001"
    answer4_string = "1011 1101 1011"
    correct_answer = "1"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)
    
    question_string = "Choose the correct ciphertext obtained after encrypting the plaintext 0010 0111 1001 using the key 1001 0110 1100"
    answer1_string = "0011 0101 1101"
    answer2_string = "1011 0001 0101"
    answer3_string = "0111 1101 0001"
    answer4_string = "1011 1101 1111"
    correct_answer = "2"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)
    
    question_string = "Choose the correct plaintext from which the ciphertext 1000 0110 0000 is obtained using the key 1100 0001 0111"
    answer1_string = "0100 0111 0111"
    answer2_string = "0101 1101 0001"
    answer3_string = "0011 1101 0001"
    answer4_string = "1011 1101 1011"
    correct_answer = "1"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)
    
    question_string = "Choose the correct plaintext from which the ciphertext 0010 1011 1111 is obtained using the key 0000 1101 1110"
    answer1_string = "0011 0101 1101"
    answer2_string = "1011 0001 0101"
    answer3_string = "0010 0110 0001"
    answer4_string = "1011 1101 1111"
    correct_answer = "3"
    new_question = Question(question_string, answer1_string,
                            answer2_string, answer3_string, answer4_string, correct_answer)
    db.session.add(new_question)
    
    
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    FillQuestionDatabase()
    app.run(debug=True)
