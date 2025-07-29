from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import os

mongo = PyMongo()

def create_app():
    app = Flask(__name__,
                template_folder=os.path.abspath("templates"),
                static_folder=os.path.abspath("static"))

    # MongoDB Config
    # app.config["MONGO_URI"] = "mongodb+srv://chanduravipati685:22K61A05E1@e-doctor.tflybyk.mongodb.net/"
    app.config["MONGO_URI"] = "mongodb://localhost:27017/e_doctor"
    mongo.init_app(app)

    # Register Blueprint for APIs (recommend, diagnose)
    from .routes import main
    app.register_blueprint(main)

    # ✅ Show welcome.html first when visiting root
    @app.route("/")
    def welcome_page():
        return render_template("welcome.html")

    # ✅ Navigation routes for other HTML pages
    @app.route("/welcome")
    def welcome():
        return render_template("welcome.html")

    @app.route("/index")
    def index():
        return render_template("index.html")

    @app.route("/diagnosis")
    def diagnosis():
        return render_template("diagnosis.html")

    @app.route("/consultation")
    def consultation():
        return render_template("consultation.html")

    @app.route("/medicine")
    def medicine():
        return render_template("medicine.html")

    @app.route("/result")
    def result():
        return render_template("result.html")

    # ✅ Handles form submission from consultation.html
    @app.route("/consultation-result", methods=["POST"])
    def consultation_result():
        first_name = request.form.get('firstName')
        contact = request.form.get('contactNumber')
        village = request.form.get('village')
        email = request.form.get('email')
        issue = request.form.get('issue')

        return render_template("result.html",
                               first_name=first_name,
                               contact=contact,
                               village=village,
                               email=email,
                               issue=issue)

    return app
