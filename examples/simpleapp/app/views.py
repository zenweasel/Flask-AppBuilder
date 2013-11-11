from flask.ext.appbuilder.menu import Menu
from flask.ext.appbuilder.baseapp import BaseApp
from flask.ext.appbuilder.views import GeneralView
from flask.ext.appbuilder.filters import *

menu = Menu()

menu.add_link(name="Google", href="http://www.google.com",icon="",parent_category="External Links")
baseapp = BaseApp(app, menu)
