from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import RedirectView
from .forms import BugCreationForm, CommentForm
from .models import Bug, Comment

def render_contact_us_page(request):
    #this function is for rendering contact_us html file
    return render(request, 'contact_us.html')
    
def display_community_page(request):
    #this function is for displaying commnuty page and rendering 3 bugs on the commuity page
    bug_view = Bug.objects.all().order_by('date_created')[:3]
    return render(request, 'community.html', {'bugs': bug_view})
 
@login_required
def render_all_bugs(request):
    # function to display all issues a on single page
    bug_view = Bug.objects.all()
    return render(request, 'display_allbugs.html', {'bugs': bug_view})

@login_required
def view_bug_details(request, id):
    # function to view one issue in detail on a template
    bug = get_object_or_404(Bug, pk=id)
    is_liked = False
     # this function also creates a comments form on the page
    if request.method == 'POST':
         form = CommentForm(request.POST)
         if form.is_valid():
             form.instance.author = request.user
             comment = form.save(commit=False)
             comment.bug = bug
             comment.save()
             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()
        
    is_liked = False
    if bug.votes.filter(id=request.user.id).exists():
        is_liked
    else:
        is_liked = True 
    context = {
        'bug': bug,
        'c_form': form,
        'is_liked': is_liked
        }
        
    return render(request, 'bugview.html', context)

@login_required  
def like_a_bug_post(request):
    bug = get_object_or_404(Bug, id=request.POST.get('bug_id'))
    is_liked = False
    if bug.votes.filter(id=request.user.id).exists():
        bug.votes.remove(request.user)
        is_liked
    else:
        bug.votes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(bug.get_absolute_url())
        
@login_required
def bug_form_page(request):
    #this function is for creating bugform and display the bugform page
    if request.method == "POST":
        form = BugCreationForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            messages.success(request, "Your Issue has been Submitted!")
            form.save()
            return redirect(reverse('allissues'))
    else:
        form = BugCreationForm() 
    return render(request, 'bugform.html', {"bug_form": form})

@login_required
def edit_issue(request, id):
    bug = get_object_or_404(Bug, pk=id)
    if request.method == 'POST':
        form = BugCreationForm(request.POST, instance=bug)
        try:
            if request.user == bug.author:
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Issue has been updated')
                    return redirect('community')
            else:
                messages.warning(request, 'You cannot make changes this document you need to be the author')
        except Exception as e:
            messages.warning(request, 'Update error: {}'.format(e))
    else:
        form = BugCreationForm(instance=bug)
    
    context = {
        'form': form,
        'bug': bug
    }
   
    return render(request, 'edit_issue.html', context)
    
@login_required
def delete_issue(request, id):
    del_bug = get_object_or_404(Bug, pk=id)
    if request.user == del_bug.author:
        del_bug.delete()
        messages.success(request, 'Issue has been deleted successfully')
        return redirect(reverse('allissues'))
    else:
        messages.error(request, 'You are not allowed to delete this Issue')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    