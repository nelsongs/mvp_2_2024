import uuid

from datetime import datetime
from src.server.instance import server


class PackageModel(server.db.Model):
    __tablename__ = "packages"

    pkg_id = server.db.Column(server.db.String(32), primary_key=True)
    pkg_nome = server.db.Column(server.db.String(50), unique=True)
    pkg_last_version = server.db.Column(server.db.String(10), nullable=False)
    pkg_uploaded_at = server.db.Column(server.db.String(25), nullable=False)

    def __init__(self, pkg_id, pkg_nome, pkg_last_version, pkg_uploaded_at):
        self.pkg_id = pkg_id
        self.pkg_nome = pkg_nome
        self.pkg_last_version = pkg_last_version
        self.pkg_uploaded_at = pkg_uploaded_at

    @classmethod
    def find_by_nome(cls, nome):
        return cls.query.filter_by(pkg_nome=nome).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def save(cls, payload):
        id_hex = uuid.uuid4().hex

        package = PackageModel(
            pkg_id=id_hex,
            pkg_nome=payload['pkg_nome'],
            pkg_last_version=payload['pkg_last_version'],
            pkg_uploaded_at=payload['pkg_uploaded_at']
        )

        server.db.session.add(package)
        server.db.session.commit()

        return package

    @classmethod
    def delete(cls, nome):
        cls.query.filter_by(pkg_nome=nome).delete()
        server.db.session.commit()

    @classmethod
    def update(cls, nome, new_version, datahora):
        updated_rows = cls.query.filter_by(pkg_nome=nome).update(
            {
                'pkg_last_version': new_version,
                'pkg_uploaded_at': datahora
            }
        )
        server.db.session.commit()
