from flask_restx import fields

from src.server.instance import server

package_form = server.package_ns.model(
    "PackageForm",
    {
        "nome": fields.String()
    }
)
