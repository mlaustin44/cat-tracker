from flask import (Blueprint, g, request, make_response)

bp = Blueprint('config', __name__)

@bp.route('/config/frequency', methods=['GET'])
def get_freq():
    return "5", 200

@bp.route('/config/targets', methods=['GET'])
def get_targets():
    return {"targets": ["target1", "target2"]}, 200