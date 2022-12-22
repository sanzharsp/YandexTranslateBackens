from rest_framework.response import Response
from rest_framework import generics
from .serializers import TranslateSerializer
from .models import YandexKeyModel
from rest_framework.permissions import AllowAny
from rest_framework import status
from .utils import post as Translated, Translate
import os
from os.path import join
from dotenv import load_dotenv
from TranslateBackens.settings import BASE_DIR

dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class TranslateView(generics.GenericAPIView):
    serializer_class = TranslateSerializer
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return YandexKeyModel.objects.all()

    def get(self, *args, **kwargs) -> dict:
        return Response("ok get")

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = {'Authorization': 'Bearer {}'.format(os.environ.get('TOKEN'))}
        data =  Translated(Translate(os.environ.get('URLS'),
                            serializer.data['sourceLanguageCode'],
                            serializer.data['targetLanguageCode'],
                            serializer.data['text'],
                            headers,
                            os.environ.get('FOLDERID'))
                           )
        if not data:
            return Response({"code": 400, "text": "NO TEXT"}, status.HTTP_400_BAD_REQUEST)
        return Response({"code": 201, "text": data}, status.HTTP_200_OK)


# Create your views here.
