from flask import jsonify
from apps.home import blueprint
from apps import db  
from apps.home.models import RawMalware
from sqlalchemy.sql import func

@blueprint.route('/malware-data')
def malware_data():
    # Query the count of samples by filetype using SQLAlchemy
    filetype_counts = db.session.query(
        RawMalware.filetype, 
        func.count(RawMalware.filetype)
    ).group_by(RawMalware.filetype).all()

    # Convert the result to a list of dictionaries
    data = [{'filetype': filetype, 'count': count} for filetype, count in filetype_counts]
    print(data)
    # Return the data as JSON
    return jsonify(data)