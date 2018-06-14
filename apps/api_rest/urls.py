from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from apps.api_rest.views import ProcesoViewSet, ProcesoDetail

from rest_framework.documentation import include_docs_urls

merouter = merouters.DefaultRouter()
merouter.register(r'procesos', ProcesoViewSet)

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='ETL CCE')),
    url(r'^proceso/(?P<pk>[0-9]+)/$', ProcesoDetail.as_view()),
]

urlpatterns += merouter.urls