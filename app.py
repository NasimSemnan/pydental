from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-in-production"


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/contact")
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    service = request.form.get("service", "").strip()

    if not name or not email or not service:
        flash("Please complete your name, email, and service preference.", "danger")
        return redirect(url_for("home") + "#appointment")

    flash(
        f"Thanks, {name.split()[0]}! We received your request and will be in touch shortly.",
        "success",
    )
    return redirect(url_for("home") + "#appointment")


if __name__ == "__main__":
    app.run(debug=True)
