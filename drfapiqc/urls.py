from django.contrib import admin
from django.urls import path, include, reverse
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('reports.urls')),
    path('', include('companies.urls')),
    path('', include('reporttankmovil.urls')),
    path('docs/', include_docs_urls(title='documentation API')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
