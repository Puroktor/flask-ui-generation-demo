from flaskUIGenerator import FlaskUIGenerator
from flask import Flask
from routes import blueprint1, blueprint2

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5000

app = Flask(__name__)
generator = FlaskUIGenerator()

app.register_blueprint(blueprint1)
generator.register_blueprint(blueprint1)

app.register_blueprint(blueprint2)
generator.register_blueprint(blueprint2)

if __name__ == '__main__':
    base_url = f'http://{DEFAULT_HOST}:{DEFAULT_PORT}'
    generator.write_config(base_url)
    app.run(debug=True, host=DEFAULT_HOST, port=DEFAULT_PORT)
