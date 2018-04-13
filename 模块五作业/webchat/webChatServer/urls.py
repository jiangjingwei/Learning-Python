from views import *


def routes():

    urlpatterns = (
        ('^/index', index),

        ('^/login', login),
        ('^/chat', chat),
        ('^/webchat', webchat),
        ('^/.*[(.jpg),(.png),(.css),(.js),(.gif),(.woff?v=3.2.1),(.ttf?v=3.2.1)]$', templates),

    )

    return urlpatterns

