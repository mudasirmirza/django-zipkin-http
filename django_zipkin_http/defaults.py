from django.conf import settings
from constants import DEFAULT_ZIPKIN_SERVICE_NAME, \
    DEFAULT_ZIPKIN_ID_GENERATOR_CLASS, DEFAULT_ZIPKIN_HTTP_API, DEFAULT_ZIPKIN_HTTP_HOST, \
    DEFAULT_ZIPKIN_HTTP_SPAN, DEFAULT_ZIPKIN_DATA_STORE_CLASS

ZIPKIN_DATA_STORE_CLASS = getattr(settings, 'ZIPKIN_DATA_STORE_CLASS', DEFAULT_ZIPKIN_DATA_STORE_CLASS)
ZIPKIN_SERVICE_NAME = getattr(settings, 'ZIPKIN_SERVICE_NAME', DEFAULT_ZIPKIN_SERVICE_NAME)
ZIPKIN_ID_GENERATOR_CLASS = getattr(settings, 'ZIPKIN_ID_GENERATOR_CLASS', DEFAULT_ZIPKIN_ID_GENERATOR_CLASS)

ZIPKIN_HTTP_HOST = getattr(settings, 'ZIPKIN_HTTP_HOST', DEFAULT_ZIPKIN_HTTP_HOST)
ZIPKIN_HTTP_API = getattr(settings, 'ZIPKIN_HTTTP_API', DEFAULT_ZIPKIN_HTTP_API)
ZIPKIN_HTTP_SPAN = getattr(settings, 'ZIPKIN_HTTP_SPAN', DEFAULT_ZIPKIN_HTTP_SPAN)

