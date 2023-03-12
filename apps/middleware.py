from __future__ import unicode_literals

from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x


class NotUseCsrfTokenMiddlewareMixin(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)


class RequestMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code >= 500:
            # todo 可以做相关处理
            pass
        return response
