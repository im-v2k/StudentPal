from django.shortcuts import render, redirect, get_object_or_404
from groups.models import Invite, CustomGroup
from django.contrib.auth.models import User
from groups.forms import *

def mygroups(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        pending_invites = Invite.objects.filter(invitee=user, is_rejected=False, is_accepted=False)
        for invite in pending_invites:
            if "accept_"+str(invite.group.pk) in request.POST:
                invite.is_accepted=True
                invite.save()
            if "reject_"+str(invite.group.pk) in request.POST:
                invite.is_rejected=True
                invite.save()
        return redirect('my_groups')
    else:
        user = User.objects.get(username=request.user)
        accepted_invites = Invite.objects.filter(invitee=user, is_accepted=True)
        pending_invites = Invite.objects.filter(invitee=user, is_rejected=False, is_accepted=False)
        rejected_invites = Invite.objects.filter(invitee=user, is_rejected=True)
        search_form = search_group()
        return render(request, 'groups/mygroups.html', {'accepted_invites' : accepted_invites,
                                                        'pending_invites' : pending_invites,
                                                        'rejected_invites' : rejected_invites,
                                                        'search_form' : search_form})

def newgroup(request):
    if request.method == 'POST':
        form = new_group(request.POST)
        if form.is_valid:
            #form.save()
            user = User.objects.get(username=request.user)
            name = request.POST.get('name')
            description = request.POST.get('description')
            group = CustomGroup.objects.create(name=name, description=description)
            invite = Invite.objects.create(sender=user, invitee=user, group=group, is_accepted=True)
            return redirect('my_groups')
    else:
        form = new_group()
    return render(request, 'groups/newgroup.html', {'form' : form})

def searchgroups(request):
    if request.method == 'POST':
        form = search_group(request.POST)
        if form.is_valid:
            string = request.POST.get('string')
            groups = CustomGroup.objects.filter(name__contains=string)
            return render(request, 'groups/searchgroups.html', {'groups' : groups, 'string' : string})
    else:
        return redirect('my_groups')

def particulargroup(request, pk):
    if request.method == 'POST':
        form = new_course(request.POST)
        if form.is_valid():
            form.save()
            group = get_object_or_404(CustomGroup, pk=pk)
            name = request.POST.get('name')
            fc = FakeCourse.objects.create(group=group, name=name)
            group.fakecourse_set.add(fc)
            user = User.objects.get(username=request.user)
            accepted_invites = Invite.objects.filter(group=group, is_accepted=True)
            check = Invite.objects.filter(group=group, invitee=user, is_accepted=True)
            courses = group.fakecourse_set.all()
            form = new_course()
            return render(request, 'groups/particulargroup.html', {'accepted_invites' : accepted_invites, 'group' : group, 'check' : check, 'courses': courses, 'form' : form})
    else:
        user = User.objects.get(username=request.user)
        group = get_object_or_404(CustomGroup, pk=pk)
        accepted_invites = Invite.objects.filter(group=group, is_accepted=True)
        check = Invite.objects.filter(group=group, invitee=user, is_accepted=True)
        form = new_course()
        courses = group.fakecourse_set.all()
        return render(request, 'groups/particulargroup.html', {'accepted_invites' : accepted_invites, 'group' : group, 'check' : check, 'form' : form, 'courses': courses})
