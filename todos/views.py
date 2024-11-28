from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import DestroyAPIView
from .tasks import send_welcome_email

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_welcome_email.delay(user.email)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            tokens = serializer.validated_data
            return Response({
                'access': tokens['access'],
                'refresh': tokens['refresh'],
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateTodoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListTodoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateTodoView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        todo = super().get_object()
        if todo.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this To-Do.")
        return todo


class DeleteTodoView(DestroyAPIView):
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        todo = super().get_object()
        if todo.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this To-Do.")
        return todo

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Todo deleted successfully"}, status=status.HTTP_200_OK)
    
# celery -A todo_project worker --pool=solo --loglevel=info
