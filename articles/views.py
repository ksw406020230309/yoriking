from rest_framework.views import APIView


# articles/
class ArticleView(APIView):
    """
    게시글 전체 목록 조회
    """

    def get(self, request):
        pass

    """
    게시글 작성
    """

    def post(self, request):
        pass


# articles/<int:article_id>/
class ArticleDetailView(APIView):
    """
    게시글 상세보기
    """

    def get(self, request, article_id):
        pass

    """
    게시글 수정하기
    """

    def put(self, request, article_id):
        pass

    """
    게시글 삭제하기
    """

    def delete(self, request, article_id):
        pass


# articles/<int:article_id>/comments/
class CommentView(APIView):
    """
    댓글 조회
    """

    def get(self, request):
        pass

    """
    댓글 작성
    """

    def post(self, request):
        pass


# articles/comments/<int:comment_id>/
class CommentDetailView(APIView):
    """
    댓글 수정
    """

    def put(self, request, comment_id):
        pass

    """
    댓글 삭제
    """

    def delete(self, request, comment_id):
        pass


# articles/<int:article_id>/like/
class LikeView(APIView):
    """
    게시글 좋아요
    """

    def post(self, request, article_id):
        pass