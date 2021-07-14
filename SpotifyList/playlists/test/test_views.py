from django.test import TestCase
from django.test import Client


from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth import *
#from django.utils.importlib import import_module
from django.conf import settings

from playlists.views import *

import requests
 
class LoginTestCase(TestCase):
        
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12')
        self.user.save()
 
    def tearDown(self):
        self.user.delete()
 
    def test_login_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)
 
    def test_login_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)
 
    def test_login_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
 


class SpotifyAuthenticationTestCase(TestCase):
 
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12')
        self.user.save()
 
    def tearDown(self):
        self.user.delete()
 
    def test_login_spotify_genius(self):
        response = requests.get("http://127.0.0.1:8000/playlists/login_spotify/")
        self.assertEquals(response.status_code, 200)

        response_genius = requests.get("http://127.0.0.1:8000/playlists/login_genius/")
        self.assertEquals(response_genius.status_code, 200)

    def test_cerrarsesion(self):
        response = requests.get("http://127.0.0.1:8000/playlists/cerrarsesion/")
        self.assertEquals(response.status_code, 200)

    def test_infoartista(self):
        response = requests.get("http://127.0.0.1:8000/playlists/info_artista/5f7VJjfbwm532GiveGC0ZK/track_name%3DWants%20and%20Needs%20(feat.%20Lil%20Baby)/")
        self.assertEquals(response.status_code, 200)

# PROBLEMA CON EL ACCESS_TOKEN

    #def test_mostrar_playlists(self):
     #   response = requests.get("http://127.0.0.1:8000/playlists/mostrar_playlists/")
     #   self.assertEquals(response.status_code, 200)



    #def test_playlist_detail(self):
     #   response = requests.get("http://127.0.0.1:8000/playlists/playlist_detail/47RwPX4akLGe6OqyGpcWMd/Rap%20Caviar/")
     #   self.assertEquals(response.status_code, 200)


    #def test_home(self):
        #response = requests.get("http://127.0.0.1:8000/playlists/home")
        #self.assertEquals(response.status_code, 200)
