# from flask import Flask,request,url_for,redirect,session,Response,render_template
# app=   Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# if __name__=="__main__":
#     app.run(debug=True)





from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def users():
    return jsonify([
        {"name": "Rahul"},
        {"name": "Aman"}
    ])

app.run(debug=True)