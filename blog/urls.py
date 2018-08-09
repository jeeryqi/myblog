from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='bloglist'),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name='blogdetail'),
    path('blog/blogtype/<int:pk>', views.BlogTypeList.as_view(), name='blogtypelist')
]
