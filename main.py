from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load the JSON data from a file
with open('C:\Geeks\PythonFlask\DPM\dpm.json', 'r') as file:
    data = json.load(file)

@app.route('/')
def index():
    keys = data.keys()
    return render_template('index.html', keys=keys)

@app.route('/get_options', methods=['POST'])
def get_options():
    selected_key = request.form.get('key')
    options = [item['option'] for item in data[selected_key]]
    return jsonify({'options': options})

@app.route('/get_details', methods=['POST'])
def get_details():
    selected_key = request.form.get('key')
    selected_option = request.form.get('selected_option')
    
    for option in data[selected_key]:
        if option['option'] == selected_option:
            return jsonify({
                'calculated': option['Calculated'],
                'partial': option['Partial'],
                'programmed_params': option['ProgrammedParametersOnPump']
            })

    return jsonify({})

if __name__ == '__main__':
    app.run(host="localhost", port=5896, debug=True)
