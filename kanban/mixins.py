from django.contrib.auth.mixins import UserPassesTestMixin

class OnlyYouMixin(UserPassesTestMixin):
    # 制限に引っかかった場合に例外を発生
    raise_exception = True

    # TrueかFalseを返す
    def test_func(self):
        user = self.request.user
        # ユーザーのpkとページのpkを比較
        return user.pk == self.kwargs['pk']