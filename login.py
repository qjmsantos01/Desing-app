from flask import Flask, request, render_template, redirect

app = Flask(__name__, static_url_path='')

@app.route("/", methods = ["GET","POST"])
def user_login():
    #reqUserLog = request.form['Username']
    #reqPassLog = request.form['Password']
    if request.method == 'POST':
        if verify_cred(reqUserLog, reqPassLog):
            return render_template("LoggendIn.html")
        else:
            error = 'Invalid username/password'
    else:
        error = 'Invalid Method'
    return render_template("login.html")

if __name__== "__main__":
    app.run(host="0.0.0.0",port=5050)