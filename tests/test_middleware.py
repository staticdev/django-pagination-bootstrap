from django.http import HttpRequest

from .test_http_request import TestHttpRequest
from django_pagination_bootstrap import middleware


def test_get_page() -> None:
    obj = TestHttpRequest()
    assert middleware.get_page(obj) == 1


def test_get_page_invalid() -> None:
    assert middleware.get_page(HttpRequest()) == 1


def test_init() -> None:
    pagination_middleware = middleware.PaginationMiddleware("response")
    assert (pagination_middleware.get_response) == "response"


# TODO redo testing after closed issue https://github.com/staticdev/django-pagination-bootstrap/issues/246
# def test_pagination_middleware(mocker: MockFixture) -> None:
#     request = mocker.Mock()
#     request.__class__.return_value = 5
#     pagination_middleware = middleware.PaginationMiddleware(mocker.Mock())
#     # CALL MIDDLEWARE ON REQUEST HERE
#     pagination_middleware(request)
#     assert request.__class__.page == 5
