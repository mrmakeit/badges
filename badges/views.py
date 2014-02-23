from django.conf import settings
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from badger.models import Award
from django.contrib.auth.models import User

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {}, RequestContext(request))


def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('/badges/')
    return render_to_response('home.html', {
    }, RequestContext(request))

@login_required
def user(request):
    """user view, displays user information"""
    user = get_object_or_404(User, username=request.user)
    awards = Award.objects.filter(user=user)
    return render_to_response('user.html',{ 
		'user': user,
		'award_list': awards,
    }, RequestContext(request))

@login_required
def badges(request):
    """Login complete view, displays user data"""
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('done.html', {
        'user': request.user,
    }, RequestContext(request))
