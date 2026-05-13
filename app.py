from flask import Flask, render_template, request, redirect, url_for, session
from entity.user_account import db, UserAccount
from entity.fundraising_activity import FundRaisingActivity
from control.auth_controller import auth_bp
from control.user_admin_controller import user_admin_bp
from control.fundraiser_controller import fundraiser_bp

app = Flask(__name__, template_folder="boundary/templates", static_url_path="/boundary/static")
app.secret_key = "secret_key"
app.register_blueprint(auth_bp)
app.register_blueprint(user_admin_bp)
app.register_blueprint(fundraiser_bp)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if not UserAccount.query.filter_by(username="admin").first():
        user = UserAccount(username="admin", password="123", role="User Admin", status="Active")

        db.session.add(user)
        db.session.commit()

if __name__=="__main__":
    app.run(debug=True)