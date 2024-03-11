from django.urls import path

from apps.web.views.auth.login import login
from apps.web.views.auth.logout import logout
from apps.web.views.auth.register import register
from apps.web.views.home import home
from apps.web.views.view_1.delete_many_by_id import delete_many_by_id
from apps.web.views.view_1.delete_many_by_id_raw_query import \
    delete_many_by_id_raw_query
from apps.web.views.view_1.delete_one_by_id import delete_one_by_id
from apps.web.views.view_1.delete_one_by_id_raw_query import \
    delete_one_by_id_raw_query
from apps.web.views.view_1.get_all import get_all
from apps.web.views.view_1.get_all_raw_query import get_all_raw_query
from apps.web.views.view_1.get_by_id import get_by_id
from apps.web.views.view_1.get_by_id_raw_query import get_by_id_raw_query
from apps.web.views.view_1.insert_many import insert_many
from apps.web.views.view_1.insert_many_raw_query import insert_many_raw_query
from apps.web.views.view_1.insert_one import insert_one
from apps.web.views.view_1.insert_one_raw_query import insert_one_raw_query
from apps.web.views.view_1.update_many_by_id import update_many_by_id
from apps.web.views.view_1.update_many_by_id_raw_query import \
    update_many_by_id_raw_query
from apps.web.views.view_1.update_one_by_id import update_one_by_id
from apps.web.views.view_1.update_one_by_id_raw_query import \
    update_one_by_id_raw_query

app_name = "web"

urlpatterns = [
    path(route="", view=home, name="home"),
    # path(route="", view=get_all, name="home"),

    # Auth
    path(
        route="register/",
        view=register,
        name="register",
    ),
    path(
        route="login/",
        view=login,
        name="login"
    ),
    path(
        route="logout/",
        view=logout,
        name="logout"
    ),

    # 1 - delete
    # path(route="page-1/<int:id>", view=delete_many_by_id, name="delete_many_by_id"),
    # path(route="page-1/<int:id>", view=delete_many_by_id_raw_query,
    #      name="delete_many_by_id_raw_query"),
    path(
        route="page-1/delete-one-by-id/<int:id>",
        view=delete_one_by_id,
        name="delete_one_by_id"
    ),
    # path(route="page-1/<int:id>", view=delete_one_by_id_raw_query,
    #      name="delete_one_by_id_raw_query"),

    # 1 - get
    path(
        route="page-1/",
        view=get_all,
        name="get_all"
    ),
    path(
        route="page-1-raw-query/",
        view=get_all_raw_query,
        name="get_all_raw_query"
    ),
    path(
        route="page-1/<int:id>",
        view=get_by_id,
        name="get_by_id"
    ),
    # path(route="page-1/<int:id>", view=get_by_id_raw_query,
    #      name="get_by_id_raw_query"),

    # 1 - insert
    # path(route="page-1/insert-many", view=insert_many, name="insert_many"),
    # path(route="page-1/insert-many-raw-query", view=insert_many_raw_query,
    #      name="insert_many_raw_query"),
    path(
        route="page-1/insert-one",
        view=insert_one,
        name="insert_one"
    ),
    # path(route="page-1/insert-one-raw-query", view=insert_one_raw_query,
    #      name="insert_one_raw_query"),

    # 1 - update
    # path(route="page-1/<int:id>", view=update_many_by_id, name="update_many_by_id"),
    # path(route="page-1/<int:id>", view=update_many_by_id_raw_query,
    #      name="update_many_by_id_raw_query"),
    path(route="page-1/update-one-by-id/<int:id>",
         view=update_one_by_id, name="update_one_by_id"),
    # path(route="page-1/<int:id>", view=update_one_by_id_raw_query,
    #      name="update_one_by_id_raw_query"),
]
