from django.test import TestCase, Client
from .models import MyVideo, Comment
from django.contrib.auth.models import User
from datetime import date
import logging

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

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

    #def test_all_video(self):
    #   response = self.client.get('/hello/')
    #   all_video = MyVideo.objects.all()
    #   all_video = [video.to_json() for video in all_video]
    #   for video in all_video:
    #       del video['long_post']
    #   for video in response.context['all_video']:
    #       del video['long_post']
    #   self.assertEqual(response.context['all_video'], all_video)


class VideoTestSeleniumLocal(TestCase):
    def setUp(self):
        super().setUp()
        self.selenium = WebDriver()
        self.live_server_url = 'http://127.0.1:8000/admin/login/'

    def tearDown(self):
        super().tearDown()
        self.selenium.quit()

    def test_selenium(self):
        self.selenium.get(self.live_server_url)
        self.selenium.implicitly_wait(10)
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('bogdan')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('gd0d469s')
        btn = self.selenium.find_element_by_xpath('//input[@value="Войти"]')
        btn.click()
        self.assertEqual(self.selenium.title, "Администрирование сайта | Административный сайт Django")
    
    def next_test(self):
        self.selenium.get(self.live_server_url)
        self.selenium.implicitly_wait(10)
        username_input = self.selenium.find_element_by_css('#id_username')
        username_input.send_keys('bogdan')
        password_input = self.selenium.find_element_by_css('#id_password')
        password_input.send_keys('gd0d469s').submit()
        self.assertEqual(self.selenium.title, "Администрирование сайта | Административный сайт Django")

    def hw_test(self):
        self.selenium.get('http://127.0.1:8000/hello/')
        self.selenium.find_element_by_xpath('html/body/a[1]').click()
        self.assertEqual(self.selenium.title, "hello video")


class VideoTestSeleniumGlobal(TestCase):
    def setUp(self):
        super().setUp()
        self.selenium = webdriver.Remote(
            command_executor = "http://172.18.0.2:4444/wd/hub",
            desired_capabilities = {"browserName":'chrome'})
        self.live_server_url = "web://web:8000/admin/login/"

    def tearDown(self):
        super().tearDown()
        self.selenium.quit()

    def test_selenium(self):
        self.selenium.get(self.live_server_url)
        self.selenium.implicitly_wait(10)
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('bogdan')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('gd0d469s')
        btn = self.selenium.find_element_by_xpath('//input[@value="Log in"]')
        btn.click()
        self.assertEqual(self.selenium.title, "Site administration | Django site admin")
# Create your tests here.
