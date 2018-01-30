from flask_login import current_user
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Separator, Text


class UserGreeting(Text):
    def __init__(self):
        pass

    @property
    def text(self):
        return 'Hello, {}'.format(current_user.name)


def main_nav():
    print('main_nav')
    return Navbar(
        View('Home', 'frontend.serve_pages', page='index')
    )


def login_nav():
    extended_nav = list(main_nav().items)
    print('login_nav')
    if current_user.is_authenticated:
        extended_nav.extend([
            Subgroup(
                'Upload',
                View('Upload Images', 'frontend.serve_pages', page='upload'),
                Separator(),
            ),
            UserGreeting(),
            View('Log out', 'security.logout')
        ])
        print('login authenticated')
    else:
        extended_nav.append(
            View('Log in', 'frontend.serve_pages', page='login'),
        )
        print('login not authenticated')
    return Navbar('main_nav', *extended_nav)


def init_nav(app):
    nav = Nav(app)
    nav.register_element('main_nav', main_nav)
    nav.register_element('main_nav', login_nav)
    nav.init_app(app)
