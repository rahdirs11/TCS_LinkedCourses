from application import app, db
from flask import render_template, url_for, request, json, Response
from application.models import User, Course, Enrollment

courseData = [
        {"courseID": "1111", "title": "PHP 111", "description": "Intro to PHP", "credits": "3", "term": "Fall, Spring"},
        {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": "4", "term": "Spring" },
        {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": "3", "term": "Fall" },
        {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": "3", "term": "Fall, Spring" },
        {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": "4", "term": "Fall" }
    ]


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)

@app.route("/user")
def user():
    User(user_id=1, first_name="Sridhar", last_name="N.S", email="sri@uta.com", password="abc1234").save()
    User(user_id=2, first_name="Deepak", last_name="Kumar", email="deeps@uta.com", password="1234abc").save()

    users = User.objects.all()
    return render_template("user.html", users=users)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', home=True)

@app.route('/courses')
@app.route('/courses/<term>')
def courses(term="Spring 2019"):
    return render_template('courses.html', courseData=courseData, courses=True, term=term)

@app.route('/register')
def register():
    return render_template('register.html', register=True)

@app.route('/login')
def login():
    return render_template('login.html', login=True)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    if request.method == "GET":
        data = request.args
    elif request.method == "POST":
        data = request.form
    return render_template('enrollment.html', data={d: data[d] for d in data})

@app.route('/api')
@app.route('/api/')
@app.route('/api/<idx>')
def api(idx=None):
    jsonData = None
    if idx == None:
        jsonData = courseData
    else:
        if int(idx) in range(1, len(courseData) + 1):
            jsonData = courseData[int(idx) - 1]
        
    
    return Response(json.dumps(jsonData), mimetype='application/json')