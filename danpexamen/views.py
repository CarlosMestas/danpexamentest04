from django.shortcuts import render
from .notification import InputForm
from django.http import HttpResponse


def notification_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "notification.html", context)


def home(request):
    return HttpResponse('Hello World')

def push_notification(request):
    from pusher_push_notifications import PushNotifications
    pn_client = PushNotifications(
        instance_id='b6dd6a14-bd22-4988-9af4-0e17301cd078',
        secret_key='947034E6EE915B5FE14519DE5DA8AA71E4C1B4C3092AA1156A481D8E3D461AB6',
    )

    response = pn_client.publish(
        interests=['hello'],
        publish_body={
            'apns': {
                'aps': {
                    'alert': 'Nueva notificación'
                }
            },
            'fcm': {
                'notification': {
                    'title': str(request.POST.get('title')),
                    'body': str(request.POST.get('text'))
                }
            }
        }
    )

    print(response['publishId'])
