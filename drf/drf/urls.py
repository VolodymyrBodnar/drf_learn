from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    re_path(r'^api/token/auth/', obtain_jwt_token),
    re_path(r'^api/token/refresh/', refresh_jwt_token),
    re_path(r'^api/token/verify/', verify_jwt_token),

]
