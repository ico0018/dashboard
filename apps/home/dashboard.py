from flask import jsonify
from apps.home import blueprint
from apps import db  
from apps.home.models import RawMalware
from sqlalchemy.sql import func

import pandas as pd

@blueprint.route('/malware-data')
def malware_data():
    # Query the count of samples by filetype using SQLAlchemy
    filetype_counts = db.session.query(
        RawMalware.filetype, 
        func.count(RawMalware.filetype)
    ).group_by(RawMalware.filetype).all()

    # Convert the result to a list of dictionaries
    data = [{'filetype': filetype, 'count': count} for filetype, count in filetype_counts]

    # Return the data as JSON
    return jsonify(data)

@blueprint.route('/process_user_queries/<user_id>')
def process_user_queries(user_id):

    user_queries_sql = f"SELECT query_id FROM user_queries WHERE user_id = {user_id}"
    user_query_ids = pd.read_sql_query(user_queries_sql, db.engine)['query_id'].tolist()

    results = []

    for query_id in user_query_ids:
        # Modify the SQL query to select both 'query' and 'title'
        query_sql = f"SELECT query, title FROM queries WHERE id = {query_id}"
        result = pd.read_sql_query(query_sql, db.engine).iloc[0]

        # Extract both 'query' and 'title' from the result set
        query = result['query']
        query_title = result['title']

        # Execute the query to get the data
        df = pd.read_sql_query(query, db.engine)
        data = df.to_dict(orient='records')

        # Append the results including the 'query_title'
        results.append({
            'query_title': query_title,
            'data': data
        })

        print(results)

    return jsonify(results)
