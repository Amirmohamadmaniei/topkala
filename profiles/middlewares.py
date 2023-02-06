from product.models import IP


class GetIPMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            ip = IP.objects.get(ip=ip)
        except IP.DoesNotExist:
            ip = IP.objects.create(ip=ip)

        request.user.ip_address = ip

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
