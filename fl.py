from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def show():
    return render_template("flaskk.html")

app.run(use_reloader=False)
