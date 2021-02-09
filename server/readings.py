from flask import (Blueprint, g, request, make_response)
from server.db import get_db
import time

bp = Blueprint('readings', __name__)

@bp.route('/reading/<source>', methods=['POST'])
def new_reading(source):
    req_data = request.get_json()
    uuid = req_data.get('uuid')
    name = req_data.get('name')
    timestamp = int(time.time())
    rssi = req_data.get('rssi')

    db = get_db()
    db.execute(f"INSERT INTO readings (source, uuid, bname, btimestamp, rssi) VALUES ('{source}', '{uuid}', '{name}', {timestamp}, {rssi})")
    db.commit()
    return "OK", 200

@bp.route('/reading/<source>/last', methods=['GET'])
def get_last_reading(source):
    db = get_db()
    reading = db.execute(f"SELECT * FROM readings WHERE source='{source}' ORDER BY id DESC LIMIT 1").fetchone()
    resp = {
        "id": reading['id'],
        "source": reading['source'],
        "uuid": reading['uuid'],
        "name": reading['bname'],
        "timestamp": reading['btimestamp'],
        "rssi": reading['rssi'] }
    return resp, 200

@bp.route('/reading/<source>/all', methods=['GET'])
def get_all_reading(source):
    as_text = True if request.args.get('text') == 'true' else False

    db = get_db()
    reading = db.execute(f"SELECT * FROM readings WHERE source='{source}'").fetchmany(3000)

    res = 'id,source,uuid,name,timestamp,rssi\n'
    for r in reading:
        res += f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]},{r[5]}\n"

    if as_text:
        return res, 200
    else:
        response = make_response(res)
        response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
        response.mimetype='text/csv'
        return response, 200

    