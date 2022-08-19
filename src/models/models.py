from sqlalchemy.sql import func
from flask_login import UserMixin
from .. import db


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    password = db.Column(db.String(100))
    expenses = db.relationship('Expense', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.id}>'


class ExpenseCategory(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<ExpenseCategory {self.id, self.name}>'


class Expense(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('expense_category.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())

    def __repr__(self):
        return f'<Expense {self.id, self.amount}>'