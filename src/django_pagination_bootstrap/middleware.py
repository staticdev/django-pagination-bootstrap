"""django-pagination-bootstrap middleware."""


def get_page(self) -> int:
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current page.
    """
    try:
        return int(self.GET.get("page"))
    except (KeyError, ValueError, TypeError):
        return 1


class PaginationMiddleware:
    """Pagination Middleware class.

    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> None:
        request.__class__.page = property(get_page)
