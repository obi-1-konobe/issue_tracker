from django.db import models


class Issue(models.Model):
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

    author = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Author',
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

    performer = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default='Unknown',
        verbose_name='Performed by'
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