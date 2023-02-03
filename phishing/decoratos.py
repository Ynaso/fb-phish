from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def allow_cors(func):
    @method_decorator(csrf_exempt)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    return wrapper