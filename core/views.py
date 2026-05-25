from django.shortcuts import render
from django.http import JsonResponse
from .models import user
import json

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tg_user = data.get('user')
        print(tg_user)

        if tg_user:
            user_obj, created = user.objects.update_or_create(
                ids=tg_user.get('id'),
                defaults={
                    'username': tg_user.get('username'),
                    'first_name': tg_user.get('first_name'),
                    'last_name': tg_user.get('last_name'),
                    'profile_pic': tg_user.get('photo_url', ''), # Assuming photo_url is what you want for profile_pic
                }
            )
            if created:
                user_obj.balance = 0.00
                user_obj.save()

            return JsonResponse({'status': 'ok', 'message': 'User data saved.'})
        return JsonResponse({'status': 'error', 'message': 'User data not provided.'}, status=400)

    return render(request, 'home.html')