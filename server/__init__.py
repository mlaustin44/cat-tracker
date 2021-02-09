import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_path=os.path.join(os.getcwd(), 'server', 'instance'))

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'cat.db')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import readings
    app.register_blueprint(readings.bp)

    from . import config
    app.register_blueprint(config.bp)
    
    @app.route('/reading/<source>', methods=['POST'])
    def new_reading(source):
        pass

    @app.route('/hello', methods=["GET"])
    def hello():
        return "Why hello there!"
    
    return app