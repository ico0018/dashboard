from flask import render_template
from apps.home import blueprint

@blueprint.route('/map')
def show_map():
    # This is a mock function, you would replace this with actual database calls
    partners_coordinates = [
        {"latitude": 40.7128, "longitude": -74.0060},  # New York
        {"latitude": 34.0522, "longitude": -118.2437},  # Los Angeles
        {"latitude": 51.5074, "longitude": -0.1278}    # London
    ]
    
    return render_template('home/map.html', partners_coordinates=partners_coordinates)
