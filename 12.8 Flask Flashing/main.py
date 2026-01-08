from flask import Flask, render_template, flash, redirect

app = Flask(__name__)

app.secret_key = "321adgjkbdh4heg6s8ndtuj3h4gds"

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/logout")
def logout():
    flash("You have been logged out!", "success")
    return render_template('logout.html')

app.run(debug=True)
