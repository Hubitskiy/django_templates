from django import forms
from video.models import Comment
from video.models import MyVideo

class CommentForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	text.widget.attrs.update({'class': 'form-control'})

	def save(self, user_id, video_id):
		if self.is_valid():
			Comment.objects.create(
				text=self.cleaned_data['text'],
				user_id = user_id,
				video_id = video_id
			)
			return True
		return False


class VideoForm(forms.Form):
	vid_title = forms.CharField()
	vid_slug = forms.SlugField()
	vid_description = forms.CharField(widget=forms.Textarea)
	vid_url = forms.URLField()

	vid_title.widget.attrs.update({'class': 'form-control'})
	vid_slug.widget.attrs.update({'class': 'form-control'})
	vid_description.widget.attrs.update({'class': 'form-control'})
	vid_url.widget.attrs.update({'class': 'form-control'})

	def save(self):
		if self.is_valid():
			MyVideo.objects.create(
				title = self.cleaned_data['vid_title'],
				slug = self.cleaned_data['vid_slug'],
				description = self.cleaned_data['vid_description'],
				url = self.cleaned_data['vid_url']
			)
			return True
		return False

class NeEbstisVideo(forms.ModelForm):
	class Meta:
		model = MyVideo
		fields = ['title', 'slug', 'description', 'url']
		widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
				   'slug': forms.TextInput(attrs={'class':'form-control'}),
				   'description':forms.TextInput(attrs={'class':'form-control'}),
				   'url': forms.TextInput(attrs={'class':'form-control'})
				   }