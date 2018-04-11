from views import *


def routes():

    urlpatterns = (
        ('^/index', index),

        ('^/login', login),
        ('^/.*[(.jpg),(.png),(.css),(.js),(.gif)]$', templates),

    )

    return urlpatterns

