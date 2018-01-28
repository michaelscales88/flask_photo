from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Separator


def get_nav(app):
    nav = Nav(app)
    nav.register_element('main_nav', Navbar(
            View('Home', 'frontend.serve_pages', page='index'),
            # Subgroup(
            #     '',
            #     Separator(),
            # ),
        )
    )
    return nav
