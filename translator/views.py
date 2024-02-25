from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status


from .transliterator import transliterate
from .models import TextTrans, FileTrans
from .serializers import TextTransSerializer, FileTransSerializer


class TextView(CreateAPIView):
    queryset = TextTrans
    serializer_class = TextTransSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        if 'context' in data and 'pattern' in data:
            context = data['context']
            pattern = data['pattern']

            if pattern == 'cyrillic':
                result = transliterate(context, from_='lat', to='cyr')
            elif pattern == 'latin':
                result = transliterate(context, from_='cyr', to='lat')

            else:
                return Response({'error': 'Invalid pattern!'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'result': result}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid request!'}, status=status.HTTP_400_BAD_REQUEST)


class FileView(CreateAPIView):
    queryset = FileTrans
    serializer_class = FileTransSerializer

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        pattern = request.data['pattern']

        if file.name.endswith('.txt'):
            data = file.read().decode('utf-8')

            if pattern == 'cyrillic':
                result = transliterate(data, from_='lat', to='cyr')
            elif pattern == 'latin':
                result = transliterate(data, from_='cyr', to='lat')

            else:
                return Response({'error': 'Invalid pattern!'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'result': result}, status=status.HTTP_200_OK)


