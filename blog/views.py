from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import post
from .forms import postform


# Create your views here.

def post_list(request):
    posts = post.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request,pk):
    postc = get_object_or_404(post,pk=pk)
    post.objects.get(pk=pk)
    return render(request,'blog/post_detail.html',{'postc':postc})

def post_new(request):
    if request.method =="POST":
        form = postform(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_details',pk=post.pk)
        else:
            form = postform()
            return render(request,'blog/post_edit.html',{'form': form})

def post_edit(request,pk):
    postb = get_object_or_404(post,pk=pk)
    if request.method=="POST":
        form = postform(request.POST,instance=postb)
        if form.is_valid():
            postb=form.save(commit=False)
            postb.author=request.user
            postb.save()
            return redirect('post_detail',pk=postb.pk)
        else:
            form = postform(instance=postb)
            return render(request,'blog/post_edit.html',{'form':form})
def post_draft_list(request):
    posts=post.objects.filter(publishedDate__isnull=True).order_by('createdDate')
    return render(request,'blpg/post_draft_list.html',{'posts':post})

def post_publish(request,pk):
    posta = get_object_or_404(post,pk=pk)
    posta.publish()
    return redirect('post_detail',pk=pk)

def publish(self):
    self.publishedDate = timezone.now()
    self.save()

def post_remove(request, pk):
    postd=get_object_or_404(post,pk=pk)
    postd.delete()
    return redirect('post_list')
