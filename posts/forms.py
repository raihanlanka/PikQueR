from django import forms
from .models import PostDetail,Comment


class imageuploadform(forms.ModelForm):
	class Meta:
		model=PostDetail
		fields =["postpicture",]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)