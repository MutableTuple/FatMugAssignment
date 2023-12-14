# from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project,Review

@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET":"/api/projects"},
        {"GET":"/api/projects/id"},
        {"POST":"/api/projects/id/vote"},
        {"POST":"/api/users/token"},
        {"POST":"/api/users/token/refersh"},
    ]
    return Response(routes)

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    print("USER",request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True) #serializer data into JSON data
    return Response(serializer.data)

# single projects
@api_view(["GET"])
def getProject(request,pk):
    projects = Project.objects.get(id=pk)
    serializer = ProjectSerializer(projects, many=False) #serializer data into JSON data
    return Response(serializer.data)

@api_view(["POST","PUT"])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    projects = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    
    review,created = Review.objects.get_or_create(
        owner = user,
        project = projects
    )
    review.value = data['value']
    review.save()
    projects.getVoteCount
    serializer = ProjectSerializer(projects, many=False) #serializer data into JSON data
    return Response(serializer.data)
