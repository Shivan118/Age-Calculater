from flask import Flask, render_template, request
from datetime import datetime, date
import calendar  # Import calendar module
from utils.age import calculate_age

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    age_data = None
    if request.method == 'POST':
        birth_year = int(request.form['birth_year'])
        birth_month = int(request.form['birth_month'])
        birth_day = int(request.form['birth_day'])
        age_data = calculate_age(birth_year, birth_month, birth_day)
    return render_template('index.html', age_data=age_data, current_year=datetime.now().year, calendar=calendar)

if __name__ == "__main__":
    app.run(debug=True)
