import io
from unittest.mock import Mock
from unittest.mock import patch

from django.core.handlers.wsgi import WSGIRequest
from django.test import TestCase

from django_pagination_bootstrap import middleware


class TestPaginationMiddleware(TestCase):
    @patch("django_pagination_bootstrap.middleware.PaginationMiddleware")
    def test_init(self, pagination_middleware_mock: Mock):
        pagination_middleware = middleware.PaginationMiddleware("response")
        request = WSGIRequest(
            {
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": "multipart",
                "wsgi.input": io.StringIO(),
            }
        )
        assert pagination_middleware.__call__(request)
