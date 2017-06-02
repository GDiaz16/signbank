from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.forms.models import model_to_dict
from django.http import HttpResponseForbidden
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.sites.shortcuts import get_current_site
from django.dispatch import receiver
from django_comments.models import Comment
from django_comments.signals import comment_was_posted
from django_comments.forms import CommentForm
from django_comments import get_model as django_comments_get_model
from tagging.models import Tag


class CommentTagForm(forms.Form):
    """Form for tags, meant to be used when adding tags to Comments."""
    tag = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False, empty_label="---", to_field_name='name',
                                 widget=forms.Select(attrs={'class': 'form-control'}))


def edit_comment(request, id):
    """View to bind comment data to form and update comment."""
    comment = get_object_or_404(Comment, id=id)
    # Make sure that only the commenter can edit the comment.
    if not request.user == comment.user:
        return HttpResponseForbidden(_("You are not allowed to edit this comment, "
                                       "because you are not the author of the comment."))
    if request.method == 'POST':
        form = EditCommentForm(request.POST)
        if form.is_valid():
            comment.comment = form.cleaned_data["comment"]
            comment.save()
        if 'HTTP_REFERER' in request.META:
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(request.path)

    else:
        return bind_comment(request, comment)


def bind_comment(request, comment):
    """Bind the data into the form."""
    commdict = model_to_dict(comment)
    form = CommentForm(comment, commdict)
    return render(request, 'comments/edit_comment.html', {'form': form})


class EditCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


def latest_comments_page(request, count=20):
    if int(count) > 100:
        count = 100
    qs = django_comments_get_model().objects.filter(
        site__pk=get_current_site(request).pk,
        is_public=True,
        is_removed=False,
    ).order_by('-submit_date')[:count]
    return render(request, 'comments/latest_comments_page.html', {'comments': qs})


def latest_comments(request):
    qs = django_comments_get_model().objects.filter(
        site__pk=get_current_site(request).pk,
        is_public=True,
        is_removed=False,
    ).order_by('-submit_date')[:10]
    return render(request, 'comments/latest_comments.html', {'comments': qs})


@receiver(comment_was_posted, sender=Comment)
def add_tags_to_comments(sender, request, comment, **kwargs):
    """Add tags to a comment after comment has been created."""
    if request.method == 'POST':
        form = CommentTagForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["tag"]:
                Tag.objects.add_tag(comment, form.cleaned_data["tag"].name)
