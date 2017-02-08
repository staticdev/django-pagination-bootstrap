def get_page(self):
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current page.
    """
    try:
        return int(self.GET.get('page'))
    except (KeyError, ValueError, TypeError):
        return 1


class PaginationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    """
    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """
    def __call__(self, request):
        request.__class__.page = property(get_page)
        return self.get_response(request)
