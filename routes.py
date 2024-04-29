from flask import Blueprint, request, jsonify
from flaskUIGenerator import display_name
from flaskUIGenerator.decorators import request_body, query_param, response_body, path_param

from dto import TestDto2, TestDto1, TestStatus

blueprint1 = Blueprint("controller1", __name__, url_prefix="/api/controller1")
blueprint2 = Blueprint("controller2", __name__, url_prefix="/api/controller2")


@blueprint1.route("/entity", methods=["POST", "PUT"])
@request_body(TestDto1)
def create_entity():
    return jsonify()


@blueprint1.route("/entity", methods=["GET"])
@display_name("Retrieve entity")
@query_param(int, "id", "Entity ID")
@response_body(TestDto1)
def get_entity():
    entity_id = int(request.args.get("id"))
    test_dto2 = TestDto2(description1="Example description 1", description2="Example description 2")
    test_dto1 = TestDto1(id=entity_id, flag=True, status=TestStatus.SECOND, text_list=["hi", "hello"],
                         test_dto2=test_dto2)
    return jsonify(test_dto1)


@blueprint2.route("/example/<entity_id>", methods=["DELETE"])
@display_name("Another example method")
@path_param("entity_id", "Entity ID")  # Optional, can be omitted
@query_param(int, "id2")
@response_body(TestDto2)
def delete_entity(entity_id: int):
    return jsonify({
        "description1": str(entity_id),
        "description2": request.args.get("id2"),
    })
