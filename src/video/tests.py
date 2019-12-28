from django.test import TestCase, Client
from .models import MyVideo, Comment
from django.contrib.auth.models import User
from datetime import date
import logging


class VideoTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		video = MyVideo.objects.create(
			id=1,
			title="test title",
			slug='test_slug',
			description="test description",
			url='https://www.test_url.duck')
		user = User.objects.create(
			id=1,
			username="Test Username")
		user.set_password('password')
		user.save()
		Comment.objects.create(
			id=1,
			text="comment test 1",
			video=video,
			user=user)
		Comment.objects.create(
			id=2,
			text='comment test 2',
			video=video,
			user=user)

	def test_have_str(self):
		video = MyVideo.objects.get(id=1)
		self.assertEqual(video.__str__(), f"{video.title} - {video.slug[:10]}")

	def test_have_comments(self):
		video = MyVideo.objects.get(id=1)
		all_comments = Comment.objects.filter(video=video)
		self.assertCountEqual(video.comment, all_comments)

	def test_long_post(self):
		video = MyVideo.objects.get(id=1)
		current_response = date.today() - video.date.date()
		self.assertEqual(video.long_post, current_response)

	def test_hello_page(self):
		response = self.client.get('/hello/')
		self.assertEqual(response.status_code, 200)

	def test_fail_page(self):
		response = self.client.get('/rtfghf/')
		self.assertEqual(response.status_code, 404)

	def test_authenticate(self):
		res = self.client.login(
			username='Test Username',
			password='password')
		self.assertEqual(res, True)

	def test_content(self):
		self.client.login(
			username='Test Username',
			password='password')
		response = self.client.get('/hello/')
		self.assertEqual(response.context['user'].username, 'Test Username')
		#logging.warning(response.context)

	def test_all_video(self):
		response = self.client.get('/hello/')
		all_video = MyVideo.objects.all()
		all_video = [video.to_json() for video in all_video]
		for video in all_video:
			del video['long_post']
		for video in response.context['all_video']:
			del video['long_post']
		self.assertEqual(response.context['all_video'], all_video)



# Create your tests here.
