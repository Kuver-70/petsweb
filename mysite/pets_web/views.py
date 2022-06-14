from .models import Post, Pet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, PetForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id')) # post_id - это значение name элемента button из шаблона post.html
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('pets_web:post_detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    #user_id = Pet.objects.get('author')

    def get_context_data(self, *args, **kwargs): # Попробовать такую же конструкцию для целей выбора из "своих" питомцев при создании поста.
        context = super(PostDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class PostAddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_add.html'
    #context_object_name = ''
    # Переменная post передается автоматически. Т.к. мы использовали модель Post.
    #fields = '__all__'
    #fields = ('author', 'title', 'text') # теперь не нужно указывать поля, т.к. в форме это указано


class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_update.html'
    #fields = ['title', 'text']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('pets_web:home') # URL при удалении поста. Т.к. при удалении обычная reverse в models.py не работает и выдает ошибку


'''def index(request):
    latest_post_list = Post.objects.order_by('-published_date')[:5]
    #output = '<br>'.join([p.title for p in latest_post_list])
    #template = loader.get_template('pets_web/index.html')
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'pets_web/index.html', context)


def post(request, post_id):
    #responce = "You're looking on post %s."
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pets_web/post.html', {'post': post})


def post_new(request):
    return HttpResponse("Here you can create new post.")
'''