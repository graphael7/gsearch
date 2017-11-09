from django.conf.urls  import  include, url
from .views import ColorList
from color_liker.views import toggle_color_like

urlpatterns = [

    url(r'^$', ColorList.as_view(), name="color_list"),

    url(r'^like_color_(?P<color_id>\d+)/$', toggle_color_like, name='toggle_color_like'),

]
