from flask import Blueprint


blueprint = Blueprint("routes", __name__, url_prefix="/api")


@blueprint.route("/query")
def query_api():
    pass
