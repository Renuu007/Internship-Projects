from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    # Optional: log the incoming alert
    print('Received alert:', request.json)
    # Run the Ansible playbook (update the path as needed)
    result = subprocess.run([
        'ansible-playbook', '/playbooks/recover_nginx.yml'
    ], capture_output=True, text=True)
    print('Ansible output:', result.stdout)
    print('Ansible errors:', result.stderr)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
