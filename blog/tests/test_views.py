from django.test import TestCase
from django.urls import reverse
from blog.models import Post

class HomeViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Published Post", content="Yes", published=True)
        Post.objects.create(title="Unpublished Post", content="No", published=False)

    def test_home_view_status_and_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_home_view_context_contains_only_published(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Published Post")
        self.assertNotContains(response, "Unpublished Post")
