from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


def register(request):
    """ view displaying customer registration form """
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            #form.save()
            user = form.save(commit=False)  # new
            user.save()  # new
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = reverse('accounts:profile')
                return HttpResponseRedirect(url)
    else:
        #TODO: already logged in case
        form = UserCreationForm()
    page_title = 'User Registration'
    return render_to_response('registration/create_user.html', locals(), context_instance=RequestContext(request))


@login_required
def profile(request):
    return render_to_response('accounts/real_profile.html', locals())