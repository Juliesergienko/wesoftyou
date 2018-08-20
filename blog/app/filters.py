from django_filters import rest_framework as filters

from blog.app.models import Post


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', ]
