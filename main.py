from flask import Flask
from flasgger import Swagger
from routes.users import users_blueprint
from routes.travel import travel_blueprint

app = Flask(__name__)

# Initialize Swagger with custom configuration
swagger = Swagger(app, template={
    "info": {
        "title": "Tax Residency Application",
        "version": "1.0",
        "description": "API documentation for the Tax Residency Application"
    }
})

# Register blueprints
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(travel_blueprint, url_prefix='/travel')

if __name__ == '__main__':
    app.run(debug=True)