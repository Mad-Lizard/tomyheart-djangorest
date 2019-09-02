from rest_framework import serializers
from recovery.models import Post, Article, Athlet
from django.contrib.auth.models import User

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = [
                  'created_at',
                  'published_at',]

        created_by = serializers.ReadOnlyField(source='created_by.username')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class AthletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlet
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'post_set']
    #by default the namr of the attribute should be model_set
    post_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
