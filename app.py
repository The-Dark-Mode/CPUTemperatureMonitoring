from flask import Flask, render_template, jsonify
import subprocess
import re

app = Flask(__name__)

def get_temperatures():
    result = subprocess.run(['sensors'], stdout=subprocess.PIPE)
    sensors_output = result.stdout.decode('utf-8')
    
    core_temps = re.findall(r'Core \d+:\s+\+(\d+\.\d+)°C', sensors_output)
    core_temps = [float(temp) for temp in core_temps]
    
    return core_temps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    core_temps = get_temperatures()
    return jsonify({"temperatures": core_temps})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
