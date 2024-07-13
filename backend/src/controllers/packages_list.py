from flask_restx import Resource

from src.controllers.dto.package import package_dto
from src.models.package import PackageModel
from src.schemas.package import PackageSchema
from src.server.instance import server

ns = server.package_ns


@ns.route("/packages")
class PackagesListController(Resource):

    @ns.marshal_list_with(package_dto)
    def get(self):
        packages = PackageModel.find_all()

        return PackageSchema(many=True).dump(packages)
