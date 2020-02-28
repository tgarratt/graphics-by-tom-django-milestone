from django.conf.urls import url, include
from unpurchasable.views import get_unpurchasable, get_unpurchasable_logo, get_unpurchasable_clothing, get_unpurchasable_web_app, get_unpurchasable_advertising, get_unpurchasable_illustration, get_unpurchasable_piece, get_unpurchasable_piece_delete, get_unpurchasable_piece_edit

urlpatterns = [
    url(r'^$', get_unpurchasable, name='unpurchasable'), 
    url(r'^logo$', get_unpurchasable_logo, name='unpurchasable_logo'),
    url(r'^clothing$', get_unpurchasable_clothing,
        name='unpurchasable_clothing'),
    url(r'^web_app$', get_unpurchasable_web_app, name='unpurchasable_web_app'),
    url(r'^advertising$', get_unpurchasable_advertising,
        name='unpurchasable_advertising'),
    url(r'^Illistration$', get_unpurchasable_illustration,
        name='unpurchasable_illustration'),
    url(r'^unpurchasable_piece/(?P<pk>\d+)', get_unpurchasable_piece,
        name='unpurchasable_piece'),
    url(r'^unpurchasable_piece_delete/(?P<pk>\d+)',
        get_unpurchasable_piece_delete, name='unpurchasable_piece_delete'),
    url(r'^unpurchasable_piece_edit/(?P<pk>\d+)', get_unpurchasable_piece_edit,
        name='unpurchasable_piece_edit'),
    ]

    