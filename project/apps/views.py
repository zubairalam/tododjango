from django.shortcuts import render

from django.http import HttpResponse

import logging

logger = logging.getLogger("management")

def my_view(request):
    logger.info("this is a management logging info")
    return HttpResponse(status=200)
