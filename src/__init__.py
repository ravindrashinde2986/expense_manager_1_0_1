from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user

db = SQLAlchemy()
migrate = Migrate()


def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', user=current_user), 404


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8c0832fb3d0fb59eb29fab33b54d9d91'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5434/expense_mgr_db'
    from .auth.auth import auth_bp
    from .dashboard.dashboard import dashboard_bp
    from .expenses.expenses import expenses_bp
    app.register_blueprint(auth_bp, static_url_path='../../static')
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(expenses_bp, url_prefix='/expenses')
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager = LoginManager()
    login_manager.login_view = 'auth_bp.login'
    login_manager.login_message_category = 'error'
    login_manager.init_app(app)
    app.register_error_handler(404, page_not_found)
    from .models.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    return app
