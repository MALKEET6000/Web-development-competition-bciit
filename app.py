from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)



# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grades = db.relationship('Grade', backref='student', lazy=True)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    
# Create database
with app.app_context():
    db.create_all()



@app.route('/index', methods=['POST'])
def home():
    return render_template('index.html')
def register():
    data = request.json
    new_user = User(email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'}), 201

@app.route('/add_grade', methods=['POST'])
def add_grade():
    data = request.json
    new_grade = Grade(student_id=data['student_id'], score=data['score'])
    db.session.add(new_grade)
    db.session.commit()
    return jsonify({'message': 'Grade added successfully'}), 201

@app.route('/grades/<int:student_id>', methods=['GET'])
def get_grades(student_id):
    grades = Grade.query.filter_by(student_id=student_id).all()
    return jsonify([{'id': g.id, 'score': g.score} for g in grades]), 200

if __name__ == '__main__':
    app.run(debug=True)
