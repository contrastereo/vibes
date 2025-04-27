from django.shortcuts import render


def receive_view(request):
    """Render a page where users can request a haiku from the AI."""
    return render(request, 'api/receive.html') 