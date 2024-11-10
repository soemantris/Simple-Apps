from django.forms import ModelForm
from . models import Comment


class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = (
            'comments',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comments'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan komentar anda disini.', 'rows': 3})
