from behave import step
from pages.url_navigation_page import UrlNavigationPage


@step('url is loaded')
def homepage_nav(context):
    UrlNavigationPage(context).visit_url(context.env)

