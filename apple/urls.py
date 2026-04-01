from rest_framework.routers import DefaultRouter
from .views import Viewname

Router = DefaultRouter()
Router.register(r'backend', Viewname)
urlpatterns = Router.urls
