from flask import Flask, render_template, request, jsonify, make_response
import json
from datetime import datetime
import os

app = Flask(__name__)

def parse_time_to_hours(days, hours, minutes):
    """Convert days, hours, and minutes to total hours."""
    days_val = float(days) if days else 0
    hours_val = float(hours) if hours else 0
    minutes_val = float(minutes) if minutes else 0
    total_hours = days_val * 24 + hours_val + minutes_val / 60
    return total_hours

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        # Parse original time (free option) with safe conversion
        original_days = data.get('original_days', '0')
        original_hours = data.get('original_hours', '0')
        original_mins = data.get('original_mins', '0')
        original_total_hours = parse_time_to_hours(original_days, original_hours, original_mins)
        
        # Parse time with cost with safe conversion
        cost_days = data.get('cost_days', '0')
        cost_hours = data.get('cost_hours', '0')
        cost_mins = data.get('cost_mins', '0')
        cost_total_hours = parse_time_to_hours(cost_days, cost_hours, cost_mins)
        
        # Get cost and hourly value with safe conversion
        dollar_cost_val = data.get('dollar_cost', '0')
        hourly_value_val = data.get('hourly_value', '0')
        dollar_cost = float(dollar_cost_val) if dollar_cost_val else 0
        hourly_value = float(hourly_value_val) if hourly_value_val else 0
        
        # Calculate time saved in hours
        time_saved_hours = original_total_hours - cost_total_hours
        
        # Calculate value of time saved
        value_of_time_saved = time_saved_hours * hourly_value
        
        # Create result object
        result = {
            'original_time': f"{float(original_days) if original_days else 0}d {float(original_hours) if original_hours else 0}h {float(original_mins) if original_mins else 0}m",
            'cost_time': f"{float(cost_days) if cost_days else 0}d {float(cost_hours) if cost_hours else 0}h {float(cost_mins) if cost_mins else 0}m",
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
    # Only enable debug mode if explicitly set via environment variable
    # NEVER enable debug in production!
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
