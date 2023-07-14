from rest_framework import serializers
from .models import Issue, Agent, Mechanic


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ["agentID"]


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = ["mechanicID"]


class IssueSerializer(serializers.ModelSerializer):
    agentID = serializers.SerializerMethodField()
    mechanicID = serializers.SerializerMethodField()

    def get_agentID(self, obj):
        agent = obj.agent
        if agent:
            return agent.agentID
        return None

    def get_mechanicID(self, obj):
        mechanic = obj.mechanic
        if mechanic:
            return mechanic.mechanicID
        return None

    class Meta:
        model = Issue
        fields = [
            "issueID",
            "userID",
            "location",
            "problem",
            "time",
            "status",
            "agentID",
            "mechanicID",
        ]
