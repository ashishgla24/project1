from flask import Flask, render_template
from form import RegisterForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        mobile = form.mobile.data
        email = form.email.data
        return render_template(
            "login.html", message="Registration successful! Please login!"
        )

    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
