from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post, Message
from .forms import UploadForm, MessageForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# frontend

def search_title(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__icontains=searched)
        return render(request,
                      'search_title.html',
                      {'searched': searched,
                       'posts': posts,})
    else:
        return render(request,
                      'search_title.html',
                      {})
    ordering = ['-id']


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetails, self).get_context_data()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetails, self).get_context_data()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class UploadImage(CreateView):
    model = Post
    form_class = UploadForm
    template_name = 'upload_image.html'

def send_message(request):
    submitted = False
    if request.method == "POST":
        message = MessageForm(request.POST)
        if message.is_valid():
            message.save()
            return HttpResponseRedirect('/send_message?submitted=True')
    else:
        message = MessageForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'message.html', {
        'form': message,
        'submitted': submitted
    })

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

