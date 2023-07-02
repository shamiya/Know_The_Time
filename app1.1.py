from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        base_country = request.form['base_country']
        base_timezone = request.form['base_timezone']
        dest_country = request.form['dest_country']
        dest_timezone = request.form['dest_timezone']
        time_format = request.form['time_format']

        base_time = datetime.now(pytz.timezone(base_timezone))
        dest_time = datetime.now(pytz.timezone(dest_timezone))
        time_diff = base_time.utcoffset() - dest_time.utcoffset()
        time_diff_hours = time_diff.total_seconds() / 3600
        print("Time Difference:", time_diff_hours)

        try:
            return render_template('result.html', base_country=base_country, base_time=base_time.strftime(time_format),
                                   dest_country=dest_country, dest_time=dest_time.strftime(time_format),
                                   time_diff=str(time_diff_hours))  # Convert time_diff_hours to a string
        except Exception as e:
            print("Template rendering error:", str(e))

        return "An error occurred."
    else:
        return "Invalid request method."

if __name__ == '__main__':
    app.run(debug=True)
