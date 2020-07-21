import io

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from django.test import TestCase

from .test_http_request import TestHttpRequest
from django_pagination_bootstrap import middleware


def test_get_page() -> None:
    obj = TestHttpRequest()
    assert middleware.get_page(obj) == 1


def test_get_page_invalid() -> None:
    assert middleware.get_page(HttpRequest()) == 1


class TestPaginationMiddleware(TestCase):
    def test_init(self) -> None:
        pagination_middleware = middleware.PaginationMiddleware("response")
        request = WSGIRequest(
            {
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": "multipart",
                "wsgi.input": io.StringIO(),
            }
        )
        pagination_middleware.__call__(request)
