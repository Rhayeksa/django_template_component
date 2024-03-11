from django.db import connection, connections
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.sql_to_json import sql_to_json


@api_view(["GET"])
# @api_view(["POST"])
# @api_view(["PUT"])
# @api_view(["DELETE"])
def get_all_raw_query(request, ids: list = []):
    # cursor = connection.cursor()
    cursor = connections["default"].cursor()
    cursor.execute(
        """
        SELECT
            char_field
            , number_field
            , email_field
            , choice_field
            , text_field
        FROM table_1
        ORDER BY id_field DESC
        """
    )

    # return Response({"message": "Hello, world!"})
    # return Response({"message": cursor.fetchall()})
    return Response({"data": sql_to_json(cursor=cursor)})
