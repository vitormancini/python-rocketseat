from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id = 1

# Cria uma task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    global task_id
    new_task = Task(
        id = task_id,
        title = data['title'],
        description = data['description']
    )
    tasks.append(new_task)
    task_id += 1

    return jsonify({ 'message:': 'Nova task criada com sucesso!'}), 201

# Obtem todas as tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = [task.to_dict() for task in tasks]
    result = {
        'tasks': all_tasks,
        'total': len(tasks)
    }

    return jsonify(result), 200

# Obtem task pelo id
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict()), 200
        
    return jsonify({'message': 'Não foi possível encontrar a task!'}), 404

# Atualiza uma task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({'message': 'Não foi possível encontrar a task!'}), 404
    
    data = request.get_json()

    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    return jsonify({ 'message': 'Tarefa atualizada com sucesso!' })

# Exclui ua tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({'message': 'Não foi possível encontrar a task!'}), 404
    
    tasks.remove(task)

    return jsonify({ 'message': 'Tarefa excluída com sucesso!' })

if __name__ == '__main__':
    app.run(debug=True)