from django.http import HttpRequest


class TestHttpRequest(HttpRequest):
    """Test helper class."""

    __test__ = False
    page = 1
