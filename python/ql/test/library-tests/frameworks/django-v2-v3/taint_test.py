"""testing views for Django 2.x and 3.x"""
from django.urls import path
from django.http import HttpRequest
from django.views import View


def test_taint(request: HttpRequest, foo, bar, baz=None):  # $requestHandler routedParameter=foo routedParameter=bar
    ensure_tainted(foo, bar) # $ tainted
    ensure_not_tainted(baz)

    # Manually inspected all fields of the HttpRequest object
    # https://docs.djangoproject.com/en/3.0/ref/request-response/#httprequest-objects

    ensure_tainted(
        request,
        request.body,
        request.path,
        request.path_info,
        request.method,
        request.encoding,
        request.content_type,
        request.content_params,
        request.content_params["key"],
        request.content_params.get("key"),
        request.GET,
        request.GET["key"],
        request.GET.get("key"),
        request.GET.getlist("key"),
        request.GET.getlist("key")[0],
        request.GET.pop("key"),
        request.GET.pop("key")[0],
        request.GET.popitem()[0],
        request.GET.popitem()[1],
        request.GET.popitem()[1][0],
        request.GET.dict(),
        request.GET.dict()["key"],
        request.GET.urlencode(),
        request.POST,
        request.COOKIES,
        request.COOKIES["key"],
        request.COOKIES.get("key"),
        request.FILES,
        request.FILES["key"],
        request.FILES["key"].content_type,
        request.FILES["key"].content_type_extra,
        request.FILES["key"].content_type_extra["key"],
        request.FILES["key"].charset,
        request.FILES["key"].name,
        request.FILES["key"].file,
        request.FILES["key"].file.read(),
        request.FILES.get("key"),
        request.FILES.get("key").name,
        request.FILES.getlist("key"),
        request.FILES.getlist("key")[0],
        request.FILES.getlist("key")[0].name,
        request.FILES.dict(),
        request.FILES.dict()["key"],
        request.FILES.dict()["key"].name,
        request.META,
        request.META["HTTP_USER_AGENT"],
        request.META.get("HTTP_USER_AGENT"),
        request.headers,
        request.headers["user-agent"],
        request.headers["USER_AGENT"],
        request.resolver_match,
        request.resolver_match.args,
        request.resolver_match.args[0],
        request.resolver_match.kwargs,
        request.resolver_match.kwargs["key"],
        request.get_full_path(),
        request.get_full_path_info(),
        request.read(),
        request.readline(),
        request.readlines(),
        request.readlines()[0],
        list(request),
    )


    # django.urls.ResolverMatch also supports iterable unpacking
    _view, args, kwargs = request.resolver_match
    ensure_tainted(
        args, # $ tainted
        args[0], # $ tainted
        kwargs, # $ tainted
        kwargs["key"], # $ tainted
    )

    ensure_not_tainted(
        request.current_app,

        # Django has `ALLOWED_HOSTS` to ensure the HOST value cannot be tampered with.
        # It is possible to remove this protection, but it seems reasonable to assume
        # people don"t do this by default.
        request.get_host(),
        request.get_port(),
    )

    ####################################
    # build_absolute_uri
    ####################################
    ensure_tainted(
        request.build_absolute_uri(), # $ MISSING: tainted
        request.build_absolute_uri(request.GET["key"]), # $ MISSING: tainted
        request.build_absolute_uri(location=request.GET["key"]), # $ MISSING: tainted
    )
    ensure_not_tainted(
        request.build_absolute_uri("/hardcoded/"),
        request.build_absolute_uri("https://example.com"),
    )

    ####################################
    # get_signed_cookie
    ####################################
    # We don't consider user to be able to tamper with cookies that are signed
    ensure_not_tainted(
        request.get_signed_cookie("key"),
        request.get_signed_cookie("key", salt="salt"),
        request.get_signed_cookie("key", max_age=60),
    )
    # However, providing tainted default value might result in taint
    ensure_tainted(
        request.get_signed_cookie("key", request.COOKIES["key"]), # $ MISSING: tainted
        request.get_signed_cookie("key", default=request.COOKIES["key"]), # $ MISSING: tainted
    )


class ClassView(View):
    def some_method(self):
        ensure_tainted(
            self.request, # $ tainted
            self.request.GET["key"], # $ tainted

            self.args, # $ tainted
            self.args[0], # $ tainted

            self.kwargs, # $ tainted
            self.kwargs["key"], # $ tainted
        )


# fake setup, you can't actually run this
urlpatterns = [
    path("test-taint/<foo>/<bar>", test_taint),  # $ routeSetup="test-taint/<foo>/<bar>"
    path("ClassView/", ClassView.as_view()), # $ routeSetup="ClassView/"
]
