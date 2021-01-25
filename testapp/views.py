from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import AddPostForm
from django.views import generic

class BlogView(generic.ListView):
    template_name='testapp/Home.html'
    context_object_name='blogpost'

    def get_queryset(self):
        return Blog.objects.all()


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'testapp/BlogDetail.html'

def AddPost(request):
    #print(request)
    #form = AddPostForm()
    if request.method == "POST":
        #print(request.POST['title'])
        #data = request.POST
      form = AddPostForm(request.POST , request.FILES)
        #blog = Blog.objects.create(title = data['title'], content = data['content'])
        #blog.save()
      if form.is_valid():
          title = form.cleaned_data['title']
          content = form.cleaned_data['content']
          image = form.cleaned_data['image']
            #print(title ,content)
          author = request.user  
          blog = Blog.objects.create(title = title , content = content,author=author, image=image)
          blog.save()
          return HttpResponse('blog post created')
    else:
        #print(request.user)
        form = AddPostForm()
        blog = Blog.objects.all()
        #print(blog)
    context = { 'form': form}
    return render(request, 'testapp/AddItem.html',context)

def PostLike(request, postid):
    post = Blog.objects.get(id = postid) 
    user = request.user
    if user.is_authenticated:
        if user in post.likes.all():
            return HttpResponse('you are like this post already!')
        post.likes.add(user)   
       #return HttpResponse('you like a post')
        return redirect('detail', postid)
    else:
        return HttpResponse('you are not allow to like this post')



def PostUnLike(request, postid):
    post = Blog.objects.get(id = postid) 
    user = request.user
    if user.is_authenticated:
        if user in post.likes.all():
           post.likes.remove(user)   
           #return HttpResponse('you unlike this post')
           return redirect('detail', postid) 
        else:      
            return HttpResponse('you are not like this post') 
    else:
        return HttpResponse('you are not allow to like this post')





#def BlogView(request):
    #print(request)
    #form = AddPostForm()
#   if request.method == "POST":
#       #print(request.POST['title'])
        #data = request.POST
#       form = AddPostForm(request.POST)
        #blog = Blog.objects.create(title = data['title'], content = data['content'])
        #blog.save()
#      if form.is_valid():
#           title = form.cleaned_data['title']
#           content = form.cleaned_data['content']
            #print(title ,content)
#          blog = Blog.objects.create(title = title , content = content)
#           blog.save()
#          return HttpResponse('blog post created')
#    else:
#        form = AddPostForm()
#        blog = Blog.objects.all()
        #print(blog)
#    context = {'blogpost':blog , 'form': form}
#    return render(request, 'Home.html',context)




#def BlogDetail(request ,postid):
    #name = "codinguy"
#    post = Blog.objects.get(id=postid)
#    context = {'post':post }
    #return HttpResponse(f"hey! you are looking at {num}")#f-string
#    return render(request, 'BlogDetail.html',context)