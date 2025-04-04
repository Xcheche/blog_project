from django.test import TestCase
from django.test import TestCase
from.models import Post
from django.urls import reverse

# Create your tests here.
class UnitTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or state for the tests
        pass
    
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
        # self.assertContains(response, 'Welcome to the Blog')
        
        
        
     #About page test
     
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')
        self.assertContains(response, 'About')
        
    #latest posts test
    
    def test_latest_posts(self):
        response = self.client.get('/latest/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/latest_post.html')
        self.assertContains(response, 'Latest Posts') 
        
        
    #post detail
    
    def test_post_detail(self):
        response = self.client.get('/post_detail/')
        # response = self.client.get(f'/post/{self.post.id}/') 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        # self.assertContains(response, 'post.title')       
        
        
        
    def tearDown(self):
        return super().tearDown()    
