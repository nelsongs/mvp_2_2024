from src.server.instance import server
from src.models.package import PackageModel


class PackageSchema(server.ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PackageModel
        load_instance = True
