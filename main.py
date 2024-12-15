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

# Register blueprints with versioned URL prefix
app.register_blueprint(users_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(travel_blueprint, url_prefix='/api/v1/travel')

if __name__ == '__main__':
    app.run(debug=True)