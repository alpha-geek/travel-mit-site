from django.core.urlresolvers import reverse
from travelsite.settings import MEDIA_ROOT, MEDIA_URL
from PIL import Image as PImage
from os.path import join as pjoin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from travelsite.forum.models import *
from django.shortcuts import redirect, render_to_response
from django.template import loader, Context, RequestContext
#from django.db.models.signals import post_save
#from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.core.handlers import wsgi
#from registration.signals import user_registered


#def user_created(sender, user, request, **kwargs):
#    form = UserRegistrationForm(request.POST)
#    data = profile.PROFILE(user=user)
#    data.city_id = form.data["city"]
#    data.save()

#user_registered.connect(user_created)


@login_required
def profile_view(request):
    """Edit user profile."""
#    user_profile = request.user.get_profile()
    user_profile = get_or_create_user_profile(request) 
  # img = None

#    if request.method == "POST":
 #       pf = ProfileForm(request.POST, request.FILES, instance=profile)
   #     if pf.is_valid():
  #          pf.save()
            # resize and save image under same filename
    #        imfn = pjoin(MEDIA_ROOT, profile.avatar.name)
      #      im = PImage.open(imfn)
     #       im.thumbnail((160,160), PImage.ANTIALIAS)
     #      im.save(imfn, "JPEG")
   # else:
  #      pf = ProfileForm(instance=profile)

 #   if profile.avatar:
#        img = "/media/" + profile.avatar.name
    return render_to_response("forum/profile.html", add_csrf(request))
def login_view(request):
    return render_to_response("destinations/index.html")

def logout_view(request):
    
    return render_to_response("destinations/index.html")

#def createUserProfile(sender,instance, **kwargs):
#    UserProfile.objects.get_or_create(user=instance)
#post_save.connect(createUserProfile, sender=User)

def main(request):
    """Main listing."""
    forums = Forum.objects.all()
    return render_to_response("forum/main.html", dict(forums=forums, user=request.user))

def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get("page",'1'))
    except ValueError: page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items

def forum(request, pk):
    """Listing of threads in a forum."""
    threads = Thread.objects.filter(forum=pk).order_by("-created")
    threads = mk_paginator(request, threads, 20)
    return render_to_response("forum/forum.html", add_csrf(request, threads=threads, pk=pk))
#    return HttpResponseRedirect(reverse('forum/forum.html',

def thread(request, pk):
    posts = Post.objects.filter(thread=pk).order_by("created")
    posts = mk.paginator(request, posts, 15)
    title = Thread.objects.get(pk=pk).title
    return render_to_response("forum/thread.html", add_csrf(request, posts=posts, pk=pk, title=title, media_url=MEDIA_URL))

def post(request, ptype, pk):
    """Display a post form."""
    action = reverse("travelsite.forum.views.%s" % ptype, args=[pk])
    if ptype == "new_thread":
        title = "Start New Topic"
        subject = ''
    elif ptype == "reply":
        title = "Reply"
        subject = "Re: " + Thread.objects.get(pk=pk).title

    return render_to_response("forum/post.html", add_csrf(request, subject=subject,action=action, title=title))

def new_thread(request, pk):
    """Start a new thread."""
    p = request.POST
    if p["subject"] and p["body"]:
        forum = Forum.objects.get(pk=pk)
        thread = Thread.objects.create(forum=forum, title=p["subject"], creator=request.user)
        Post.objects.create(thread=thread, title=p["subject"], body=p["body"], creator=request.user)
    increment_post_counter(request)
    return HttpResponseRedirect(reverse("dbe.forum.views.forum", args=[pk]))

def increment_post_counter(request):
    profile = request.user.userprofile_set.all()[0]
    profile.posts += 1
    profile.save()

def reply(request, pk):
    """Reply to a thread."""
    p = request.POST
    if p["body"]:
        thread = Thread.objects.get(pk=pk)
        post = Post.objects.create(thread=thread, title=p["subject"], body = p["body"], creator=request.user)
    increment_post_counter(request) 
    return HttpResponseRedirect(reverse("travelsite.forum.views.thread", args=[pk]) + "?page=last")   
