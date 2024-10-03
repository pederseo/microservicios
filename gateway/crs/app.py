from flask import Flask
from routes.gateway_routes import gateway_bp


app = Flask(__name__)


# Registrar el Blueprint para las rutas del gateway
app.register_blueprint(gateway_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
