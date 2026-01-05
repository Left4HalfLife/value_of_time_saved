from flask import Flask, render_template, request, jsonify, make_response
import json
from datetime import datetime

app = Flask(__name__)

def parse_time_to_hours(days, hours, minutes):
    """Convert days, hours, and minutes to total hours."""
    total_hours = float(days or 0) * 24 + float(hours or 0) + float(minutes or 0) / 60
    return total_hours

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        # Parse original time (free option)
        original_days = float(data.get('original_days', 0))
        original_hours = float(data.get('original_hours', 0))
        original_mins = float(data.get('original_mins', 0))
        original_total_hours = parse_time_to_hours(original_days, original_hours, original_mins)
        
        # Parse time with cost
        cost_days = float(data.get('cost_days', 0))
        cost_hours = float(data.get('cost_hours', 0))
        cost_mins = float(data.get('cost_mins', 0))
        cost_total_hours = parse_time_to_hours(cost_days, cost_hours, cost_mins)
        
        # Get cost and hourly value
        dollar_cost = float(data.get('dollar_cost', 0))
        hourly_value = float(data.get('hourly_value', 0))
        
        # Calculate time saved in hours
        time_saved_hours = original_total_hours - cost_total_hours
        
        # Calculate value of time saved
        value_of_time_saved = time_saved_hours * hourly_value
        
        # Create result object
        result = {
            'original_time': f"{original_days}d {original_hours}h {original_mins}m",
            'cost_time': f"{cost_days}d {cost_hours}h {cost_mins}m",
            'time_saved_hours': round(time_saved_hours, 2),
            'dollar_cost': round(dollar_cost, 2),
            'hourly_value': round(hourly_value, 2),
            'value_of_time_saved': round(value_of_time_saved, 2),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
