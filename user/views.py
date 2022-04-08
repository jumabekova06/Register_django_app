from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import  status

# Create your views here.
class CreateUserView(CreateAPIView):
    queryset = User
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        token = Token.objects.get_or_create(user=account)[0].key
        data = serializer.data
        data["message"] = "user registered successfully"
        data["token"] = token

        return Response(data, status=status.HTTP_201_CREATED)