from flask import Flask, request, jsonify, send_from_directory
import subprocess, tempfile, os

# Point static_folder at your frontend folder
app = Flask(__name__,
            static_folder=os.path.join(os.path.dirname(__file__), '../frontend'),
            static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code','')
    user_input = data.get('input','')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode='w') as tmp:
        tmp.write(code); tmp.flush(); code_file = tmp.name
    try:
        result = subprocess.run(
            ["python", code_file],
            input=user_input, capture_output=True, text=True, timeout=5
        )
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)
    os.remove(code_file)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
