from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(title="Test Post", content="Test", published=True)

    def test_str_representation(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_is_published_true(self):
        self.assertTrue(self.post.is_published())
