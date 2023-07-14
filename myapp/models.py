from django.db import models


class Agent(models.Model):
    agentID = models.AutoField(primary_key=True)
    queue = models.IntegerField(default=0)

    def __str__(self):
        return f"Agent ID: {self.agentID}"


class Mechanic(models.Model):
    mechanicID = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Mechanic ID: {self.mechanicID}"


class Issue(models.Model):
    ISSUE_STATUS_CHOICES = [
        ("INQUEUE", "In Queue"),
        ("ASSIGNED", "Assigned"),
        ("DISPATCHED", "Dispatched"),
    ]

    issueID = models.AutoField(primary_key=True)
    userID = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    problem = models.TextField()
    time = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=ISSUE_STATUS_CHOICES, default="INQUEUE"
    )
    agent = models.ForeignKey(
        Agent, on_delete=models.DO_NOTHING, related_name="issues"
    )
    mechanic = models.ForeignKey(
        Mechanic,
        on_delete=models.DO_NOTHING,
        related_name="issues",
    )

    def __str__(self):
        return f"Issue ID: {self.issueID}: status: {self.status}"
