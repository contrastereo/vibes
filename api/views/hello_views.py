from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.services.hello_service import get_hello_message, get_hello_name_message
from api.services.ai_service import generate_haiku
from rest_framework import status

@api_view(['GET'])
def hello_world(request):
    """Return a hello world message."""
    message = get_hello_message()
    return Response({"message": message})

@api_view(['POST'])
def hello_name(request):
    """Return a personalized hello message."""
    name = request.data.get('name')
    message = get_hello_name_message(name)
    return Response({"message": message})

@api_view(['GET'])
def ai_haiku(request):
    """Return a generated haiku from the AI agent."""
    try:
        haiku = generate_haiku()
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"haiku": haiku}) 