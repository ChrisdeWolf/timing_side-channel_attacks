import time
from flask import Flask, request, Response, abort, render_template
# from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from collections import defaultdict

app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)
app.config['SECRET_KEY'] = 'loginexample'


class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


users = {
    1: User(1, 'Chris deWolf', 'v3rySeKr3t123'),
    2: User(2, 'user', 'pass')
}

nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
# for i in users.values():
#     user_check[i.username]['password'] = i.password
#     user_check[i.username]['id'] = i.id

# def load_user(id):
#     return users.get(int(id))

def strcmp(s1, s2):
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return False
        time.sleep(0.01)
    return True

adminUsername = 'deWolf'
adminPassword = 'v3rySeKr3t123'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        print(username)
        print(password)
        # if username in user_check and password == user_check[username]['password']:
        # if username.encode('utf-8') == adminUsername.encode('utf-8') and password.encode('utf-8') == adminPassword.encode('utf-8'):    
        if strcmp(username, adminUsername) and strcmp(password, adminPassword):
            return 'admin login success!'
        else:
            return abort(401)
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    return Response('logout success.<br/><a href="/login">login</a>')


@app.route('/')
def home():
    return Response('<a href="/login">login</a>')


if __name__ == '__main__':
    app.run(debug=True)