from views import *


def routes():

    urlpatterns = (
        ('^/index', index),

        ('^/login', login),
        ('^/chat', chat),
        ('^/.*[(.jpg),(.png),(.css),(.js),(.gif)]$', templates),

    )

    return urlpatterns

