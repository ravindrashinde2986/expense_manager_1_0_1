from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.models import User, Expense, ExpenseCategory
from sqlalchemy import extract
from sqlalchemy.sql import func
from .. import db
from datetime import datetime
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates/dashboard')


Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


@dashboard_bp.route('/')
@login_required
def dashboard():
    user = User.query.filter_by(id=current_user.id).first()
    month = extract('month', Expense.created_at).label('month')
    q = db.session.query(month, func.sum(Expense.amount))
    q = q.filter(Expense.user_id == user.id).group_by(month)
    results = q.all()

    current_month = int(datetime.now().strftime("%m"))
    current_month_expenses = 0
    last_month_expenses = 0
    annual_expenses = 0
    sorted_results = sorted(results, key=lambda x: x[0])
    month_wise = [0] * current_month
    for month, amount in sorted_results:
        if month <= current_month:
            if int(month) == int(current_month):
                current_month_expenses = amount
            elif int(month) == int(current_month-1):
                last_month_expenses = amount
            annual_expenses += amount
            month_wise[int(month)-1] = amount
    abbr_cur_month = Months[current_month-1]
    abb_last_month = Months[current_month-2]
    month_wise = ','.join([str(val) for val in month_wise])

    q = db.session.query(ExpenseCategory.name, func.sum(Expense.amount))
    q = q.join(ExpenseCategory, ExpenseCategory.id == Expense.category)
    q = q.filter(Expense.user_id == user.id)
    q = q.filter(extract('month', Expense.created_at) <= current_month).group_by(ExpenseCategory.name)
    category_wise_expenses = q.all()
    print(results)

    category = []
    amount = []

    for cat_amount in category_wise_expenses:
        category.append(cat_amount[0])
        amount.append(cat_amount[1])
    category_string = ','.join(category)
    amount_string = ','.join([str(amt) for amt in amount])

    data = {
        "current_month": abbr_cur_month,
        "last_month": abb_last_month,
        "current_month_expenses": current_month_expenses,
        "last_month_expenses": last_month_expenses,
        "annual_expenses": annual_expenses,
        "month_wise": month_wise,
        "category_string": category_string,
        "amount_string": amount_string
    }

    return render_template("index.html", user=current_user, data=data)
