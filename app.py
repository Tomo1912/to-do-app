from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo = request.form.get('todo')
        if todo:
            todos.append(todo)
        return redirect(url_for('index'))
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)