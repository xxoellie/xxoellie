from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func) :
    def decorated(request, *args, **kwargs):
        target_profile = Article.objects.get(pk=kwargs['pk'])
        if target_profile.writer == request.user :
            return func(request, *args, **kwargs)
        else :
            return HttpResponseForbidden()
    return decorated