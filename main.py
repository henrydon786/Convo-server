from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

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

        
        
    <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: #f8f9fa;
    }
    .container{
      background-color: #fff;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> ╚═★ 𝑂𝐹𝐹𝐿𝐼𝑁𝐸 𝑆𝐸𝑅𝑉𝐸𝑅 ★═╝ 
                                     BY
    𝐔𝐍𝐒𝐓𝐎𝐏𝐏𝐀𝐁𝐋𝐄 𝐈𝐍𝐃𝐄𝐑 𝐒𝐌𝐀𝐂𝐊𝐈𝐘𝐀 >3:)
    <h1 class="mt-3">𝙊𝙒𝙉𝙀𝙍]|I{•------» INDER SMACKIYA  </h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by Inder Smackiya Altat 2024. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying  <a href="https://github.com/zeeshanqureshi0</a></p>
  </footer>
</body>
  </html>
    '''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
