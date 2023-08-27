from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import viewsets

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
