"""
ASGI config for chat_reddis project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from chat import routing  # new
from .tokenauth_middleware import TokenAuthMiddleware  # new

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_reddis.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(  # new
        TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)))
})