from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    base_timezones = pytz.all_timezones
    dest_timezones = pytz.all_timezones
    return render_template('index.html', base_timezones=base_timezones, dest_timezones=dest_timezones)

@app.route('/convert', methods=['POST'])
def convert():
    base_timezone = request.form['base_timezone']
    dest_timezone = request.form['dest_timezone']
    time_format = request.form['time_format']

    base_time = datetime.now(pytz.timezone(base_timezone)).strftime('%Y-%m-%d %H:%M:%S')
    dest_time = datetime.now(pytz.timezone(dest_timezone)).strftime('%Y-%m-%d %H:%M:%S')
    time_diff = datetime.now(pytz.timezone(base_timezone)).utcoffset() - datetime.now(pytz.timezone(dest_timezone)).utcoffset()
    time_diff_hours = time_diff.total_seconds() / 3600

    return render_template('result.html', base_timezone=base_timezone, dest_timezone=dest_timezone,
                           base_time=base_time, dest_time=dest_time, time_diff=time_diff_hours)

def format_time(dt, time_format):
    if time_format == '12-hour':
        return dt.strftime('%Y-%m-%d %I:%M:%S %p')
    else:
        return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)
