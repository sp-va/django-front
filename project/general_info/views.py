from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import render

from general_info.forms import FeedBackForm


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
            print("Проверка формы")
            form.save()
            return JsonResponse({"result": "successful"})
        else:
            errors = form.errors.as_json()
            return JsonResponse({"result": errors}, status=400)
    else:
        print("hello")
        form = FeedBackForm()

    return render(request, "general_info/contacts.html", {"form": form})


class BlogPage(APIView):
    pass

