from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .analyzer import analyze_message
from .models import ScannedMessage
from .serializers import MessageInputSerializer, ScannedMessageSerializer


class AnalyzeMessageView(APIView):
    def post(self, request):
        serializer = MessageInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
        text = serializer.validated_data['text']
        result = analyze_message(text)
        
        record = ScannedMessage.objects.create(
            text=text,
            score=result.score,
            risk_level=result.risk_level,
            is_scam=result.is_scam,
            flags=result.flags,
            explanation=result.explanation,
        )
        
        return Response(ScannedMessageSerializer(record).data,
                        status=status.HTTP_201_CREATED)


class RecentScansView(APIView):
    def get(self, request):
        scans = ScannedMessage.objects.all()[:20]
        return Response(ScannedMessageSerializer(scans, many=True).data)


def dashboard(request):
    return render(request, 'detector/index.html')
