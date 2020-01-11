import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


TASKS = [
    {
        'id': uuid.uuid4().hex,
        'task': '777x Design build',
        'status': 'requirment',
        'deadline':'10 days remaining'
    },
    {
        'id': uuid.uuid4().hex,
        'task': '737MAX AOA design',
        'status': 'test',
        'deadline':'50 days remaining'
    },
    {
        'id': uuid.uuid4().hex,
        'task': 'NMA part configuration',
        'status': 'requirment',
        'deadline':'5 days remaining'
    },
    {
        'id': uuid.uuid4().hex,
        'task': '787 system test',
        'status': 'design',
        'deadline':'20 days remaining'
    },
    {
        'id': uuid.uuid4().hex,
        'task': 'poc work',
        'status': 'review',
        'deadline':'2 days remaining'
    },
    
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_task(task_id):
    for task in TASKS:
        if task['id'] == task_id:
            TASKS.remove(task)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/tasks', methods=['GET', 'POST'])
def all_task():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TASKS.append({
            'id': uuid.uuid4().hex,
            'task': post_data.get('task'),
            'status': post_data.get('status'),
            'deadline': post_data.get('deadline')
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)


@app.route('/tasks/<task_id>', methods=['PUT', 'DELETE'])
def single_task(task_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_task(task_id)
        TASKS.append({
            'id': uuid.uuid4().hex,
            'task': post_data.get('task'),
            'status': post_data.get('status'),
            'deadline': post_data.get('deadline')
        })
        response_object['message'] = 'Task updated!'
    if request.method == 'DELETE':
        remove_task(task_id)
        response_object['message'] = 'Task removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()