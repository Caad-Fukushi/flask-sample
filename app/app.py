from flask import Flask,render_template, request, url_for, redirect
from models.models import TaskContent
from models.database import db_session
from sqlalchemy import exc, desc
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    task_list = TaskContent.query.filter_by(status=0).order_by(desc(TaskContent.create_datetime)).all()
    return render_template("list.html",tasks=task_list)

@app.route("/task/done/<id>")
def done(id):
    task = TaskContent.query.filter_by(id=id).first()
    task.status = 1
    session.commit()
    task_list = TaskContent.query.filter_by(status=0).order_by(desc(TaskContent.create_datetime)).all()
    return render_template("list.html",tasks=task_list)

@app.route("/task/<id>")
def show(id):
    task = TaskContent.query.filter_by(id=id).first()
    return render_template("show.html",task=task)

@app.route('/add')
def add_tasks():
    return render_template('add.html')

@app.route('/delete/<id>')
def delete_task(id):
    msg=""
    task = TaskContent.query.filter_by(id=id).first()
    try:
        db_session.delete(task)
        db_session.commit()
        msg = "タスクを削除しました！"
    except exc.IntegrityError as e:
        db_session.rollback()
        msg = "タスクの削除に失敗しました"

    # task_list = TaskContent.query.all()
    return redirect(url_for('index')) 

@app.route('/add',methods=['post'])
def add_tasks_post():
    msg = ""
    task_name = request.form["task_name"]
    task_description = request.form["task_description"]
    task = TaskContent()
    task.name = task_name
    task.description = task_description
    try:
        db_session.add(task)
        db_session.commit()
        msg = "タスクの登録が完了しました！"
    except exc.IntegrityError as e:
        db_session.rollback()
        msg = "タスクが重複しています^^;"

    return render_template("add.html", alert_msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
