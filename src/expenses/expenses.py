from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models.models import Expense, ExpenseCategory
from .. import db
from sqlalchemy import cast, Date

expenses_bp = Blueprint('expenses_bp', __name__, template_folder='templates/expenses')


@expenses_bp.route('/')
@login_required
def expenses():
    q = db.session.query(Expense.id, ExpenseCategory.name, Expense.category, Expense.amount,
                         Expense.created_at.cast(Date))\
          .join(ExpenseCategory, ExpenseCategory.id == Expense.category)\
          .filter(Expense.user_id == current_user.id)
    result = q.all()

    q = db.session.query(ExpenseCategory.id, ExpenseCategory.name)
    categories = q.all()
    return render_template("expenses.html", user=current_user, data=result, len=len(result), categories=categories)


@expenses_bp.route('/edit', methods=['POST'])
@login_required
def modify_expense():
    expense_id = request.form.get('expense_id')
    expense = db.session.query(Expense).filter(Expense.id == expense_id).first()
    category_id = request.form.get('Category')
    amount = request.form.get('Amount')
    expense_date = request.form.get('ExpenseDate')
    expense.amount = amount
    expense.category = category_id
    expense.created_at = expense_date
    db.session.commit()
    return redirect(url_for("expenses_bp.expenses"))


@expenses_bp.route('/add', methods=['POST'])
@login_required
def add_expense():
    category_id = request.form.get('Category')
    amount = request.form.get('Amount')
    expense_date = request.form.get('ExpenseDate')

    expense = Expense(user_id=current_user.id, category=category_id, amount=amount, created_at=expense_date)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for("expenses_bp.expenses"))


@expenses_bp.route('/delete', methods=['POST'])
@login_required
def delete_expense():
    expense_id = request.form.get('expense_id')
    expense = db.session.query(Expense).filter(Expense.id == expense_id).first()
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for("expenses_bp.expenses"))