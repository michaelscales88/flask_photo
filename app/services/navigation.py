from flask_login import current_user
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Separator, Text


class UserGreeting(Text):
    def __init__(self):
        pass

    @property
    def text(self):
        return 'Hello, {}'.format(current_user.nickname)


def main_nav():
    nav_bar = Navbar(
        View('Home', 'frontend.serve_pages', page='index')
    )
    if current_user.is_authenticated:
        nav_bar.items.extend([
            Subgroup(
                'Upload',
                View('Upload Images', 'frontend.serve_pages', page='upload'),
                Separator(),
            ),
            View('Log out', 'logout'),
            UserGreeting()
        ])
    else:
        nav_bar.items.append(
            View('Log in', 'frontend.serve_pages', page='login'),
        )
    return nav_bar


def init_nav(app):
    nav = Nav(app)
    nav.register_element('main_nav', main_nav)
    nav.init_app(app)
