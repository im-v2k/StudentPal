from django.shortcuts import render
from groups.models import Invite, CustomGroup
from django.contrib.auth.models import User
from groups.forms import new_group

def mygroups(request):
    user = User.objects.get(username=request.user)
    accepted_invites = Invite.objects.filter(invitee=user, is_accepted=True)
    pending_invites = Invite.objects.filter(invitee=user, is_rejected=False, is_accepted=False)
    rejected_invites = Invite.objects.filter(invitee=user, is_rejected=True)

    return render(request, 'groups/mygroups.html', {'accepted_invites' : accepted_invites,
                                                    'pending_invites' : pending_invites,
                                                    'rejected_invites' : rejected_invites})

def newgroup(request):
    if request.method == 'POST':
        form = new_group(request.POST)
        if form.is_valid:
            form.save()
            name = form.cleaned_data.get('name')
            group = CustomGroup.objects.create(name=name, description=description)
            group.
