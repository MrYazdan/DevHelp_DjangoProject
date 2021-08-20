class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, r):
        import time
        start = time.time()
        response = self.get_response(r)
        end = time.time()

        print(f"{r.user} {r.user.get_full_name() if r.user.is_authenticated else '' } - {round(end - start, 2)}s")
        return response
