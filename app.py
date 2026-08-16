import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-in-production"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///appointments.sqlite3"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    service = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=True)


with app.app_context():
    db.create_all()


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/contact")
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    service = request.form.get("service", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not service:
        flash("Please complete your name, email, and service preference.", "danger")
        return redirect(url_for("home") + "#appointment")

    appointment = Appointment(
        name=name,
        email=email,
        service=service,
        message=message or None,
    )
    db.session.add(appointment)
    db.session.commit()

    flash(f"Thanks, {name.split()[0]}! We received your request and will be in touch shortly.", "success")
    return redirect(url_for("home") + "#appointment")


if __name__ == "__main__":
    app.run(debug=True)
