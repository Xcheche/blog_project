from django.test import TestCase
from django.test import TestCase
from.models import Post
from django.urls import reverse
from django.contrib.auth.models import User

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
    
    # def test_post_detail(self):
    #     response = self.client.get('/post_detail/')
    #     # response = self.client.get(f'/post/{self.post.id}/') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/post_detail.html')
    #     # self.assertContains(response, 'post.title')       
        
    def test_model_blog_post(self):
          # Import User model

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        # Create a new blog post instance
        post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            author=self.user,  # Use the created user as the author
        )
        
        # Check if the post is saved correctly
        self.assertEqual(post.title, 'Test Title')
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.author, self.user)  # Check the author is the user
        # self.assertEqual(post.slug, 'test-title')
        
        # Check if the post is saved in the database
        self.assertTrue(Post.objects.filter(title='Test Title').exists())
        
    def tearDown(self):
        return super().tearDown()    
