from flask import Blueprint, request, jsonify
import logging
from bard.logic.collections import create_collection
from bard.models.collection import Collection
from bard.app import db

log = logging.getLogger(__name__)

blueprint = Blueprint("collections_api", __name__)

@blueprint.route("/", methods=["GET"])
def index():
    """
    List of collections
    """
    return "hello"

@blueprint.route("/create", methods=["POST", "PUT"])
def create():
    collection = create_collection()
    collection.update({"label":"dfdfa"})

@blueprint.route('/collections', methods=["GET"])
def get():
    from sqlalchemy import select, column, func, table
    a = table("collection", column("label"))
    # return
    # collections = Collection.all()
    return str(a)

    # return ""
    # request_data = request.get_json()
    #
    # # summary = request_data['summary']
    # label = request_data['label']
    #
    # collection = create_collection(data=request_data)
    # resp_dictionary = {
    #     "collection_id": collection.id,
    #     "label": collection.label
    # }
    # return jsonify(resp_dictionary)

