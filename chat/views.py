from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):
    username=request.GET.get('username')  ## will ge tht e username from the url
    room_details=Room.objects.get(name=room)  ## get the particular model which has name of room (if room name is Pokemon get Pokemon model)
    return render(request,'room.html',{
        'username':username,
        'room':room,
        'room_details':room_details
    })

def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']

    ##  filter data/objects where name=room, if it exists in Room model
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save() ## as we created new object in model, we are saving it (not required, optional)
        return redirect('/'+room+'/?username='+username)


def send(request):
    message=request.POST['message']  ## this is how we get data from Ajax script that is sending data
    username=request.POST['username']  
    room_id=request.POST['room_id']

    ## adding a new entry in db
    new_message=Message.objects.create(value=message,user=username, room=room_id) 
    new_message.save()
    return HttpResponse('Message Sent Successfully')