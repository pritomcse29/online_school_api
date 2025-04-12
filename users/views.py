from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djoser import utils
from djoser.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

User = get_user_model()
class ActivateUserView(APIView):
    def get(self, request, uid, token):
        try:
            user_id = utils.decode_uid(uid)
            user = User.objects.get(pk=user_id)
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({"detail": "Account activated successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("ERROR:", e)
            return Response({"detail": "Activation failed."}, status=status.HTTP_400_BAD_REQUEST)
