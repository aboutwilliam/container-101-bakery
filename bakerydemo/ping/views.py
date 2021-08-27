import time

from django.shortcuts import render


def ping(request):
    delay = request.GET.get('delay', 0)
    error = request.GET.get('error', False)

    time.sleep(int(delay) / 1000.0)

    if error:
        raise Exception('raise a test exception')

    return render(request, 'ping/ping.html', {
        'delay': delay,
        'error': error
    })
