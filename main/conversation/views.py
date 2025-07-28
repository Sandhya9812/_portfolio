from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation
from django.shortcuts import render
import json

@csrf_exempt
def save_conversation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = data.get("question", "")
            answer = data.get("answer", "")
            if question and answer:
                Conversation.objects.create(question=question, answer=answer)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Missing data'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



def ai_assistant(request):
    return render(request, 'ai_assistant.html')
