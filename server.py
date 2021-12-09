import time
from flask import Flask, request, Response, abort, render_template
from collections import defaultdict

app = Flask(__name__)

adminUsername = 'admin'
adminPassword = 'dog'

# def constant_time_compare(val1, val2):
#     """
#     The time taken is independent of the number of characters that match.
#     """
#     if len(val1) != len(val2):
#         return False
#     result = 0
#     for x, y in zip(val1, val2):
#         result |= x ^ y  # '^' bitwise XOR, '|=' in-place OR
#     return result == 0

def strcmp(s1, s2):
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        time.sleep(.1)  # exaggerated delay for demo
        if c1 != c2:
            return False
        time.sleep(.1)
    return True

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if not password: return "missing password", 401
            
        if strcmp(password, adminPassword):
            return 'admin login success!'
        else:
            return 'login failed!'
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