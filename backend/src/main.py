from flask_cors import CORS
from src.server.instance import server
from src.controllers.package import PackagesController
from src.controllers.packages_list import PackagesListController

app = server.app

CORS(
    app,
    resources={
        r"/*": {"origins": "*"}
    }
)


if __name__ == '__main__':
    server.run(debug=False, port="8002", host="0.0.0.0")
