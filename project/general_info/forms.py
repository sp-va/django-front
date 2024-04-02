from django.forms import ModelForm

from general_info.models import Feedback


class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["email", "message"]