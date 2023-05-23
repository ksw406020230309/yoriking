from rest_framework import serializers
from articles.models import Article, Comment


# 댓글 조회
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {'nickname': obj.user.nickname, 'pk': obj.user.pk}

    class Meta:
        model = Comment
        exclude = ('article',)


# 게시글 전체 목록 조회 및 게시글 작성/수정
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return {'nickname': obj.user.nickname, 'pk': obj.user.pk}
    
    def get_comment_count(self, obj):
        return Comment.objects.filter(article=obj).count()

    def get_like_count(self, obj):
        return obj.likes.count()
    
    class Meta:
        model = Article
        fields = "__all__"


# 게시글 상세보기
class ArticleDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return {'nickname': obj.user.nickname, 'pk': obj.user.pk}
    
    def get_comment_count(self, obj):
        return Comment.objects.filter(article=obj).count()

    def get_like_count(self, obj):
        return obj.likes.count()
    
    class Meta:
        model = Article
        fields = "__all__"
        

# 댓글 작성/수정
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)