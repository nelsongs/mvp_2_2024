from flask_restx import fields

from src.server.instance import server

package_dto = server.package_ns.model(
    "PackageDTO",
    {
        "pkg_id": fields.String(),
        "pkg_nome": fields.String(),
        "pkg_last_version": fields.String(),
        "pkg_uploaded_at": fields.String()
    }
)
