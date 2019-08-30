from django.conf import settings

from django.db import models


class Issue(models.Model):
    milestone = models.ForeignKey(
        'webapp.Milestone',
        related_name='issues',
        on_delete=models.CASCADE,
        verbose_name='Milestone',
    )

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Title',
    )

    description = models.TextField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Description',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='issues',
        on_delete=models.PROTECT,

    )

    issue_type = models.ForeignKey(
        'webapp.IssueType',
        related_name='issue_types',
        on_delete=models.CASCADE,
        verbose_name='Issue type',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Time of creation',
    )
    
    started_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Start time',
    )

    ended_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='End time'
    )

    performer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='issue_performer',
        on_delete=models.PROTECT,
    )

    issue_status = models.ForeignKey(
        'webapp.IssueStatus',
        related_name='issue_statuses',
        on_delete=models.CASCADE,
        verbose_name='Issue status',
    )

    def __str__(self):
        return self.title


class IssueType(models.Model):
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Issue type',
    )

    def __str__(self):
        return self.name


class IssueStatus(models.Model):
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Issue status',
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Title',
    )

    description = models.TextField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Description',
    )

    def __str__(self):
        return self.name


class Milestone(models.Model):
    project = models.ForeignKey(
        'webapp.Project',
        related_name='milestones',
        on_delete=models.CASCADE,
        verbose_name='Project'
    )

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Title',
    )

    description = models.TextField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Description',
    )

    started_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Start time',
    )

    ended_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='End time'
    )

    def __str__(self):
        return self.name
