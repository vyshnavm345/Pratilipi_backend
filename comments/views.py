from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import CommentSerializer
# from .models import UserAccount
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from users.models import Comment, Article



@api_view(['POST'])
def make_comment(request):    
    if request.method =='POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrive_comments(request, id):
    if request.method == "GET":
        article_id = Article.objects.get(id=id)
        if article_id:
            comments = Comment.objects.filter(article=article_id)
            print(comments)
            serializer = CommentSerializer(comments, many=True)
            print("serialized : ", serializer.data)
            return Response({"Comments " : serializer.data}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_comment(request, pk):
    if request.method == 'DELETE':
        try:
            comment = Comment.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    