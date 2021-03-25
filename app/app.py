from flask import Flask, render_template
from models.models import TaskContent
from models.database import db_session
from sqlalchemy import exc, desc
app = Flask(__name__)

@app.route('/')
def index():
    task_list = TaskContent.query.filter_by(status=0).order_by(desc(TaskContent.create_datetime)).all()
    return render_template("list.html",tasks=task_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)