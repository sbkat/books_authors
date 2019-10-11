from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<book_id>\d+)$', views.books),
    url(r'^add_book$', views.add_book),
    url(r'^add_author_to_book/(?P<book_id>\d+)$', views.add_author_to_book),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<author_id>\d+)$', views.authors_profile),
    url(r'^add_author$', views.add_author),
    url(r'^add_book_to_author/(?P<author_id>\d+)$', views.add_book_to_author),
]