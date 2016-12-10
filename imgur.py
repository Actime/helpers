#Libraries
from imgurpython import ImgurClient
from events.models import Event, Galery, Competition, Price
from django.conf import settings
import os, json

#this variables are the ones that the imgur api give us after registering the aplication
client_id = 'a9e5cbb0585d300'
client_secret = '534f7fa674d788358fdced77e7e30e90336fa766'
# Set te client_id on the imgurClient method and the client_secret variables
client = ImgurClient(client_id, client_secret)

def save_image_event( file, event_id ) :
    """
    Save event image
    this method process the file for saving it to the imgur server
    Gets a file, saves it on the server, edits the model and returns nothing jet
    """
    # post on imgur and give the imgur response
    json_shit = client.upload_from_path( file, config=None, anon=True)
    # get the event with the id
    event = Event.objects.get( pk = event_id )
    # set the event image url
    event.image_url = json_shit['link']
    # save the event
    event.save()
    # remove the temporal file on the server to make space
    os.remove( file )
#End of the save_image function

def save_image_competition( file, competition_id ) :
    """
    Save competition image
    this method process the file for saving it to the imgur server
    Gets a file, saves it on the server, edits the model and returns nothing jet
    """
    # post on imgur and give the imgur response     
    json_shit = client.upload_from_path( file, config=None, anon=True)
    print( json_shit )
    # get the event with the id
    competition = Competition.objects.get( pk = competition_id )
    # set the event image url
    competition.image_url = json_shit['link']
    print(json_shit['link'])
    # save the event
    competition.save()
    # remove the temporal file on the server to make space
    os.remove( file )
#End of the save_image function

def save_image_to_galery( file, event ) :
    """
    Save galery image
    this method process the file for saving it to the imgur server
    Gets a file, saves it on the server, edits the model and returns nothing jet
    """
    # post on imgur and give the imgur response     
    json_shit = client.upload_from_path( file, config=None, anon=True)
    # set new galery model
    galery = Galery()
    # Set the event
    galery.event = event
    # Set the image url
    galery.image_url = json_shit['link']
    # Save the galery
    galery.save()
    # remove the temporal file on the server to make space
    os.remove( file )
# End of save_image_to_galery

def save_image_to_price( file, price ) :
    """
    Save image to pice table
    this method process the file for saving it to the imgur server
    Gets a file, saves it on the server, edits the model and returns nothing jet
    """
    # post on imgur and give the imgur response
    json_shit = client.upload_from_path( file, config=None, anon=True )
    # Set the image
    price.image_url = json_shit['link']
    # Save the price
    price.save()
    # remove the temporal file on the server to make space
    os.remove( file )
# End of save_image_to_price function

def save_image_conv( file, event_id ) :
    """
    Save the image to convocatory table
    this method process the file for saving it to the imgur server
    Gets a file, saves it on the server, edits the model and returns nothing jet
    """
    # post on imgur and give the imgur response
    json_shit = client.upload_from_path( file, config=None, anon=True )
    # get the event with the id 
    event = Event.objects.get( pk = event_id )
    # new convocatory table
    # set the image
    # set the event
    # save the shit
    # remove the temporal file on the server to make space daah
    os.remove( file )
# End fo save_image_conv function
