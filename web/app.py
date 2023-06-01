from flask import Flask, render_template, session, request,  redirect, url_for, flash
import datetime
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.permanent_session_lifetime = datetime.timedelta(days=365 * 2)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)