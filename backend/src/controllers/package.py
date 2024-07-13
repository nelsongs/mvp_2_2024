import requests

from flask import request
from flask_restx import Resource
from pymysql import IntegrityError
from werkzeug.exceptions import BadRequest, InternalServerError

from src.controllers.form.package import package_form
from src.controllers.dto.package import package_dto
from src.models.package import PackageModel
from src.schemas.package import PackageSchema
from src.server.instance import server

ns = server.package_ns

parser = ns.parser()
parser.add_argument("nome", type=str, location="query", required=True)


@ns.route("/package")
class PackagesController(Resource):

    @ns.expect(package_form, validate=True)
    @ns.marshal_with(package_dto)
    def post(self):
        # Chamada à API externa PyPI para verificar se o pacote existe em PyPI
        package_exists = requests.get(f"{server.API_URL}/{ns.payload['nome']}/json", timeout=6)
        if package_exists.status_code != 200:
            error_msg = "Erro: Pacote python não encontrado em PyPI"
            raise BadRequest(description=error_msg)

        try:
            # carrega as versões e suas datas de upload
            pkg_versions = package_exists.json()  # realiza parse do JSON em um dicionário

            # tratar pkg_versions para retornar apenas a última versão, sua data e hora de upload para o repositório PyPI
            versoes = self._get_versoes(pkg_versions)

            last_version = versoes[-1][1]
            datahora = versoes[-1][0]

            created_package = PackageModel.save(
                {
                    'pkg_nome': ns.payload['nome'],
                    'pkg_last_version': last_version,
                    'pkg_uploaded_at': datahora
                }
            )

            return created_package

            # Caso haja occorências de erro na inserção de dados...
        except IntegrityError as e:
            # Duplicidade de pacote
            error_msg = "Pacote python já existente na base de dados:/"
            raise BadRequest(description=error_msg)

        except Exception as e:
            error_msg = "Não foi possível adicionar o pacote python :/"
            raise BadRequest(description=error_msg)

    def _get_versoes(self, pkg_versions):
        versoes = []

        for version, files in pkg_versions["releases"].items():
            if pkg_versions["releases"][version]:  # ignora versões sem informação
                versoes.append((files[0]["upload_time"], version))

        return versoes

    @ns.expect(parser, validate=True)
    def get(self):
        nome = request.args.get("nome")

        package = PackageModel.find_by_nome(nome)

        return PackageSchema(many=False).dump(package)

    @ns.expect(parser, validate=True)
    def delete(self):
        nome = request.args.get("nome")

        package_exists = PackageModel.find_by_nome(nome)

        if package_exists:
            try:
                PackageModel.delete(nome)
            except Exception as e:
                raise InternalServerError(description="Erro interno")
        else:
            raise BadRequest(description=f"Erro ao apagar {nome}")

    @ns.expect(parser, validate=True)
    @ns.marshal_with(package_dto)
    def put(self):
        nome = request.args.get("nome")

        new_packages = requests.get(f"{server.API_URL}/{nome}/json", timeout=6).json()

        new_versions = self._get_versoes(new_packages)
        last_version = new_versions[-1][1]
        datahora = new_versions[-1][0]

        PackageModel.update(nome, last_version, datahora)

        package = PackageModel.find_by_nome(nome)
        return PackageSchema(many=False).dump(package)
