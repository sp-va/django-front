from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from general_info.forms import FeedBackForm, AddBlogForm
from general_info.models import BlogPost


class SimpleHTML(APIView): # Для эндпоинтов, возвращающих только html-шаблон
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response()


class RootPage(SimpleHTML):
    template_name = "general_info/index.html"


class AboutPage(SimpleHTML):
    template_name = "general_info/about.html"


def send_feedback(request):
    if request.method == "POST":
        data = request.POST
        form = FeedBackForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({"result": "successful"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"result": errors}, status=400)
    else:
        form = FeedBackForm()

    return render(request, "general_info/contacts.html", {"form": form})


def blog_page(request):
    if request.method == "POST":
        data = request.POST
        form = AddBlogForm(data)

        if form.is_valid():
            form.save()
            return JsonResponse({"result": "successful"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"result": errors}, status=400)

    else:
        form = AddBlogForm()
        last_blog = BlogPost.objects.order_by("created_at").reverse().first()
        if last_blog is None:
            last_blog = "Не найдено ни одной записи"

    return render(request, "general_info/blog.html", {"last_blog": last_blog, "form": form})

