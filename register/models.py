from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class Company(models.Model):
    social_name = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    found_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)


    def __str__(self):
        return (self.name)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return (str(self.user))

    def invite(self, invite_profile):

        invite = Invite(inviter=self, invited=invite_profile)
        invites = self.received_invites.filter(inviter_id=invite_profile.id)
        if not len(invites) > 0:    # don't accept duplicated invites
            invite.save()


class Invite(models.Model):
    inviter = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING ,related_name='made_invites')
    invited = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING ,related_name='received_invites')

    def accept(self):
        self.invited.friends.add(self.inviter)
        self.inviter.friends.add(self.invited)
        self.delete()

    def __str__(self):
        return str(self.inviter, 'x', self.invited)

class Friends(models.Model):
    pass