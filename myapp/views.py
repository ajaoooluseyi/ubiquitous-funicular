import random
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Issue, Agent, Mechanic
from .serializers import IssueSerializer


class CreateIssueView(APIView):
    def post(self, request):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            # Create the issue
            issue = serializer.save()

            # Assign an agent with the least requests in the queue
            agents = Agent.objects.all()
            agent_with_min_queue = agents.order_by("queue").first()
            agent_with_min_queue.queue += 1
            agent_with_min_queue.save()

            # Assign a mechanic to the issue
            mechanics = Mechanic.objects.filter(availability=True)
            if mechanics.exists():
                mechanic = random.choice(mechanics)
                mechanic.availability = False
                mechanicID = mechanic.mechanicID
                mechanic.save()
                issue.status = "DISPATCHED"
                issue.save()
            else:
                issue.status = "ASSIGNED"
                issue.save()
            
            return Response(
                {
                    "issueID": issue.issueID,
                    "agentID": agent_with_min_queue.agentID,
                    "mechanicID": mechanicID if mechanic else None,
                    "status": issue.status,
                }
            )
        return Response(serializer.errors, status=400)

    def get(self, request):
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)
