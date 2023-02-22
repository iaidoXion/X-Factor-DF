
from django.urls import path
from web.views import base_views
from common import views

urlpatterns = [
    path('', views.login, name=''),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout/'),
    path('updateform/', views.updateform, name='updateform'),
    path('update/', views.update, name='update'),
    path('dashboard/', base_views.dashboard, name='dashboard'),
    ########################### x-factor-DF ##########################################
    path('webQuery_DF/', base_views.dataFabric_webQuery, name='webQuery_DF'),
    path('monitoring_DF/', base_views.dataFabric_monitoring, name='monitoring_DF'),
    path('navigator_DF/', base_views.dataFabric_navigator, name='navigator_DF'),
    path('setting_DF/', base_views.dataFabric_setting, name='setting_DF'),
    path('webQuery_DF/query_content/', base_views.dataFabric_api, name='DF_api'),
    path('Settings_DF/setting_api/', base_views.settings_api, name='setting_api'),
    path('navigator_DF/navigator_api/', base_views.navigator_api, name='navigator_api'),
    path('navigator_DF/property_api/', base_views.property_api, name='property_api'),
    path('monitoring_DF/history_api/', base_views.hisotry_api, name='history_api'),
    path('navigator_DF/postgres_navigator_api/', base_views.postgres_navigator_api, name='postgres_navigator_api')
]