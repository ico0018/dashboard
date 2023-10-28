from flask import render_template
from apps.home import blueprint
from apps import db  
from apps.home.models import Partner  

@blueprint.route('/map')
def show_map():
    # Query for all partners' latitude and longitude using SQLAlchemy
    partners = db.session.query(Partner.latitude, Partner.longitude).filter(Partner.latitude.isnot(None), Partner.longitude.isnot(None)).all()

    # Convert the result to a list of dictionaries for compatibility with the template
    partners_coordinates = [{'latitude': p[0], 'longitude': p[1]} for p in partners]

    return render_template('home/map.html', partners_coordinates=partners_coordinates)
