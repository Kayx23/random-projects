from flask import Flask, url_for, render_template, request, session, redirect, g

app = Flask(__name__)
app.secret_key = "some_secret_key"


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


users = []
users.append(User(id=1, username='Becca', password='1234'))
users.append(User(id=2, username='Dong', password='8989'))


@app.before_request
def before_request():
    if 'user_id' in session:
        matched_user = [x for x in users if x.id == session['user_id']]
        if matched_user:
            # global object
            g.user = matched_user[0]


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop("user_id", None)
        username = request.form['username']
        password = request.form['password']
        # find the object in the list where username matches, if any
        matched_user = [x for x in users if x.username == username]
        # if username exists
        if matched_user:
            if matched_user[0].password == password:
                session['user_id'] = matched_user[0].id
                return redirect(url_for('profile'))
        # if username does not exist (empty list)
        else:
            # ADD flash()
            return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/profile')
def profile():
    user = 'Becca'
    test = 'test'
    return render_template('profile.html', user=user, test=test)
