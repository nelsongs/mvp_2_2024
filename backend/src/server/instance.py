import random
import string

from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint(
            "api",
            __name__
        )
        self.api = Api(
            self.blueprint,
            doc="/",
            title="API para o app GetLastPyPackage - Fornece a versão mais atual dos pacotes Python",
            description="Inserção, visualização e remoção na base de dados de pacotes python",
            version="1.0.0"
        )
        self.app.register_blueprint(self.blueprint)

        self.API_URL = "https://pypi.org/pypi"

        # SECRET KEY
        random_str = string.ascii_letters + string.digits + string.ascii_uppercase
        secret_key = ''.join(random.choice(random_str) for i in range(12))

        self.app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@db:3306/mvpdb"
        self.app.config["PROPAGATE_EXCEPTIONS"] = True
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.config["SECRET_KEY"] = secret_key

        self.db = SQLAlchemy(self.app)
        self.ma = Marshmallow(self.app)

        self.package_ns = self.package_ns()
        self.packages_list_ns = self.packages_list_ns()

    def package_ns(self):
        return self.api.namespace(name="Package", description="Package related operations", path="/")

    def packages_list_ns(self):
        return self.api.namespace(name="Packages list", description="Packages list related operations", path="/")

    def run(self, debug, port, host):
        self.app.run(
            debug=debug,
            port=port,
            host=host
        )


server = Server()
