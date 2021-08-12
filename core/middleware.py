class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        import time
        start = time.time()
        response = self.get_response(request)
        end = time.time()
        print(end-start)
        # Code to be executed for each request/response after
        # the view is called.

        return response
