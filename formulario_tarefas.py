from flask import Flask, render_template, request

app = Flask(__name__)

employees = ["Employee A", "Employee B", "Employee C"]
projects = ["Project X", "Project Y", "Project Z"]
tasks = ["Task 1", "Task 2", "Task 3"]
requesters = ["Requester 1", "Requester 2", "Requester 3"]

active_tasks = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-task', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        employee = request.form['employee']
        project = request.form['project']
        task = request.form['task']
        requester = request.form['requester']
        active_tasks.append((employee, project, task, requester))
    return render_template('create_task.html', employees=employees, projects=projects, tasks=tasks, requesters=requesters)

@app.route('/active-tasks')
def show_active_tasks():
    return render_template('active_tasks.html', active_tasks=active_tasks)

if __name__ == '__main__':
    app.run(debug=True)
