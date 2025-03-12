from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='todo')
    start_date = db.Column(db.DateTime, nullable=True)  # Дата начала
    end_date = db.Column(db.DateTime, nullable=True)    # Дата окончания
    assigned_users = db.relationship('User', secondary='task_user', backref=db.backref('tasks', lazy='dynamic'))



# Ассоциативная таблица для Many-to-Many связи между Task и User
task_user = db.Table('task_user',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

@app.route('/')
def index():
    now = datetime.now()  # Текущая дата
    users = User.query.all()
    todo_tasks = Task.query.filter_by(status='todo').all()
    in_progress_tasks = Task.query.filter_by(status='in_progress').all()
    done_tasks = Task.query.filter_by(status='done').all()
    return render_template('index.html', now=now, users=users, todo_tasks=todo_tasks, in_progress_tasks=in_progress_tasks, done_tasks=done_tasks)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['user_name']
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['task_name']
    description = request.form['task_description']
    start_date = request.form.get('start_date')  # Получаем дату начала
    end_date = request.form.get('end_date')      # Получаем дату окончания
    user_ids = request.form.getlist('assigned_users')

    new_task = Task(
        name=name,
        description=description,
        start_date=datetime.strptime(start_date, '%Y-%m-%d') if start_date else None,
        end_date=datetime.strptime(end_date, '%Y-%m-%d') if end_date else None
    )

    for user_id in user_ids:
        user = User.query.get(user_id)
        if user:
            new_task.assigned_users.append(user)

    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/update/<int:task_id>/<status>')
def update_task(task_id, status):
    task = Task.query.get_or_404(task_id)
    task.status = status
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/archive')
def archive():
    users = User.query.all()  # Получаем всех участников
    archived_tasks = Task.query.filter_by(status='archived').all()  # Получаем архивированные задачи
    return render_template('archive.html', users=users, archived_tasks=archived_tasks)

@app.route('/archive_task/<int:task_id>')
def archive_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'archived'  # Устанавливаем статус "archived"
    db.session.commit()
    return redirect(url_for('index'))  # Возвращаемся на главную страницу

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    users = User.query.all()

    if request.method == 'POST':
        task.name = request.form['task_name']
        task.description = request.form['task_description']
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        task.start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
        task.end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None

        task.assigned_users = []
        user_ids = request.form.getlist('assigned_users')
        for user_id in user_ids:
            user = User.query.get(user_id)
            if user:
                task.assigned_users.append(user)

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task, users=users)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('archive'))

def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized.")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)