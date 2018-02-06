from core import views
from core.auth import login
from settings import ROLE


def main():
    print('----选课系统首页----')
    # views.admin_sys('aa')
    result = login()
    if result:
        getattr(views, ROLE[result['role']])(result['user'])



