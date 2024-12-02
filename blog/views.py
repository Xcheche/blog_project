from django.shortcuts import render

# Create your views here.


def index(request):
    posts = [
        {
            "title": "Monty Python",
            "author": "Graham Chapman",
            "date": "December 12, 2020",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec nisl auctor, l",
            "image": "https://picsum.photos/200/300",
        },
    {
        "title": "The Holy Grail",
        "author": "John Cleese",
        "date": "January 15, 2021",
        "content": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.",
        "image": "https://picsum.photos/200/301",
    },
    ]
    

    return render(request, "blog/index.html", {"posts": posts})



def about(request):
    return render(request, "blog/about.html")