from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if(request.method == "POST"):
        # Handle the Form
        with open("File.txt", "w") as f:
            f.write(f"The Name is: {request.form['name']} And Email is: {request.form['email']}")
        return render_template("contact.html")
    else:
        return render_template("contact.html")

app.run(debug=True)
