from flask import Flask
from app.routes import app as routes_blueprint

app = Flask(__name__, 
            template_folder='app/templates',
            static_folder='app/static')

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Register the blueprint
app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(debug=True)