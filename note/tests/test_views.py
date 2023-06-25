import unittest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from note.models import Note
from django.urls import reverse
from http.cookies import SimpleCookie

class TestViews(TestCase):
    
    def setUp(self) -> None:
        self.guest = User.objects.create(username="guest_user")
        self.guestnote = Note(user=self.guest, title='title0',body='body0').save()
        self.guestclient = Client()
        self.guestclient.cookies = SimpleCookie({'guest': 'guest_user'})

        self.user = User.objects.create(username="user1")
        self.usernote = Note(user=self.user, title='title1', body='body1').save()
        self.userclient = Client()


    def test_index_GET(self):
        res = self.guestclient.get(reverse('note:index'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'note/index.html')
    

    def test_takenote_GET(self):
        res = self.guestclient.get(reverse('note:takenote'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'note/takenote.html')


    def test_takenote_POST(self):
        res = self.guestclient.post(
            reverse('note:takenote'),
            data={
                'title': 'title2',
                'body': 'body2'
            },
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Note.objects.get(title='title2').title, 'title2')


    def test_takenote_POST_no_data(self):
        res = self.guestclient.post(reverse('note:takenote'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Note.objects.count(), 2)


    @unittest.skip("Some shiddd happened")
    def test_detailnote_GET(self):
        res = self.guestclient.get(reverse('note:detailnote', args=[1]))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'note/detailnote.html')


    @unittest.skip("Some shiddd happened")
    def test_updatenote_POST(self):
        res = self.guestclient.post(
            reverse('note:updatenote', args=[1]),
            data={
                'title': 'title0(updated)',
                'body': 'body0(updated)'
            },
        )
        self.assertEqual(res.status_code, 302)


    def test_deletenote_POST(self):
        _ = Note(user=self.guest, title="delete_title", body="delete_body").save()
        res = self.guestclient.post(reverse('note:deletenote', args=[3]))
        self.assertEqual(Note.objects.count(), 2)