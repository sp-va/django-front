from django.forms import ModelForm

from general_info.models import Feedback, BlogPost


class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["email", "message"]


class AddBlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]
