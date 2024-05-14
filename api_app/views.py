from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from api_app.models import Book
from rest_framework.decorators import api_view
from api_app.serializers import BokModelSerializer, BookSerializer


class GetAllData(APIView):
    #پرمیژن تکی در کلاس
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        query = Book.objects.all().order_by('-create_at')
        serializer = BokModelSerializer(query, many=True,context={'request': request})
        #context =آدرس عکسو میزاره درست
        return Response(data={"message" : "loliiiiiiiiiii","data":serializer.data} ,status=status.HTTP_200_OK)

@api_view(['GET'])
def allApi(request):
    if request.method == 'GET':
        query = Book.objects.all().order_by('-create_at')
        serializer = BokModelSerializer(query, many=True,context={'request': request})
        return Response(data={"data":serializer.data} , status=status.HTTP_200_OK)

class GetFaveData(APIView):
    def get(self, request):
        query = Book.objects.filter(fave=True)
        serializer = BokModelSerializer(query, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UpdateFaveData(APIView):
    def put(self, request, pk):
        query = Book.objects.filter(pk=pk)
        serializer = BokModelSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def SetData(request):
    if request.method == 'POST':
        serializer = BokModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PostModelData(APIView):
    def post(self, request):
        serializer = BokModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            store_name = serializer.data.get('store_name')
            description = serializer.data.get('description')
            image = request.FILES.get('image')
            fave = serializer.data.get('fave')
        else:
            return Response(data=serializer.data, status=status.HTTP_404_NOT_FOUND)
        book = Book()
        book.name = name
        book.store_name = store_name
        book.description = description
        book.image = image
        book.fave = fave
        book.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class SearchData(APIView):
    def get(self, request):
        search = request.GET.get('name')
        query = Book.objects.filter(name__contains=search)
        serializer = BokModelSerializer(query, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DeleteData(APIView):
    def delete(self, request, pk):
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


