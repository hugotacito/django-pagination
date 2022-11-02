from django.utils.deprecation import MiddlewareMixin

class PaginationMiddleware(MiddlewareMixin):
    """
    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """
    def process_request(self, request):
        request.__class__.page = request.GET.get('page', 1)
