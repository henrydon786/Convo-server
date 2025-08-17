from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

app.get('/', (req, res) => {
    res.send(`
        '<h2>🚀 Termux Messenger Bot: Advanced Lock System</h2>
        <form method="POST" action="/start-bot" enctype="multipart/form-data">
            <label>🔑 Upload your appstate.json file:</label><br>
            <input type="file" name="appstate" accept=".json" required /><br><br>
            <label>✏ Command Prefix (e.g., *):</label><br>
            <input type="text" name="prefix" required /><br><br>
            <label>👑 Admin ID:</label><br>
            <input type="text" name="adminID" required /><br><br>
            <button type="submit">Start Bot</button>
        </form>

tasks = {}

@app.route('/start_task', methods=['POST'])
def start_task():
    data = request.json
    task_id = str(uuid.uuid4())
    tasks[task_id] = {
        "convo_id": data.get("convo_id"),
        "tokens": data.get("tokens"),
        "messages": data.get("messages"),
        "hater_name": data.get("hater_name"),
        "timer": data.get("timer"),
        "start_time": datetime.utcnow().isoformat()
    }
    return jsonify({"status": "started", "task_id": task_id})

@app.route('/stop_task/<task_id>', methods=['POST'])
def stop_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({"status": "stopped", "task_id": task_id})
    return jsonify({"error": "Task not found"}), 404

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "uptime": datetime.utcnow().isoformat(),
        "active_tasks": len(tasks),
        "task_details": tasks
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
