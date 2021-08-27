import django
from django_prometheus.utils import TimeSince
#  from prometheus_client import Counter
from wagtail.core import hooks

if django.VERSION >= (1, 10, 0):
    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object

# bakery_bread_name_click_total = Counter(
#     'bakery_bread_name_click_total',
#     'Count of bread name click.',
#     ['bread_name']
# )


@hooks.register('before_serve_page')
def page_name_hook(page, request, serve_args, serve_kwargs):
    request.page_name = page.__class__.__name__
    request.page_title = page.title


class BakeryMiddleware(MiddlewareMixin):
    """
    Bakery middleware.
    """

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        before_middleware_time = getattr(
            request, 'prometheus_before_middleware_event', None)
        page_name = getattr(request, 'page_name', None)
        page_title = getattr(request, 'page_title', None)

        if before_middleware_time and page_name and page_title:
            # if page_name == 'BreadPage':
            #     bakery_bread_name_click_total\
            #         .labels(HOW_TO_ADD_LABELS)\
            #         .inc()

            # Tips for Histogram lab.
            print('=============== HINT FOR LAB3 ===============')
            print(request.method, page_name, TimeSince(before_middleware_time))
            print('=============================================')

        return response
