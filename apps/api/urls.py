from django.urls import URLPattern, get_resolver, path
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.api.views.view_1.get_all_raw_query import get_all_raw_query
# from ...core.urls import urlpatterns as urlsx

# router = routers.SimpleRouter()
# router = routers.DefaultRouter()
# router.register(prefix="hunter", viewset=get_all_raw_query, basename="hunterx")


def show_urls(urllist, depth=0):
    for entry in urllist:
        print(entry.pattern)
        if hasattr(entry, 'url_patterns'):
            show_urls(entry.url_patterns, depth + 1)


@api_view(["GET"])
def home(request):
    # print(get_resolver().url_patterns)
    # print(URLPattern())
    # print(show_urls(get_resolver().url_patterns))
    return Response({"url": []})


app_name = "api"


urlpatterns = [
    path(
        route="",
        view=home,
        name="home",
    ),
    path(
        route="get-all-raw-queryX",
        view=get_all_raw_query,
        name="get_all_raw_query",
    ),
    # router.urls
]
