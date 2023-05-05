from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from .serializers import AccountSerializer
from .models import User
from .permissions import IsAuthenticatedUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
import ipdb


class RegisterView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        accounts = User.objects.all()

        result_page = self.paginate_queryset(accounts, request)

        serializer = AccountSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class RegisterDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedUser]

    def get(self, request: Request, user_id: int) -> Response:
        accounts = get_object_or_404(User, id=user_id)
        if not request.user.is_employee and user_id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = AccountSerializer(
            accounts,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


""" class LoginView(APIView):
        def post(self, request: Request) -> Response:
            serializer = TokenObtainPairSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            return Response(serializer.validated_data)


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if not user:
            return Response(
                {
                    "detail": "No active account found with the given\
                         credentials"
                },
                status.HTTP_401_UNAUTHORIZED,
            )
        refresh = RefreshToken.for_user(user)
        token = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return Response(token) """
