from django.test import SimpleTestCase
from django.urls import reverse, resolve
from note.views import IndexView, DetailNoteView, TakeNoteView, UpdateNoteView, DeleteNoteView


class TestUrls(SimpleTestCase):
    
    def test_index_resolve(self):
        url = reverse('note:index')
        r = resolve(url)
        self.assertEqual(r.func.view_class, IndexView)

    def test_takenote_resolve(self):
        url = reverse('note:takenote')
        r = resolve(url)
        self.assertEqual(r.func.view_class, TakeNoteView)

    def test_detailnote_resolve(self):
        url = reverse('note:detailnote', args=[1])
        r = resolve(url)
        self.assertEqual(r.func.view_class, DetailNoteView)

    def test_updatenote_resolve(self):
        url = reverse('note:updatenote', args=[1])
        r = resolve(url)
        self.assertEqual(r.func.view_class, UpdateNoteView)

    def test_deletenote_resolve(self):
        url = reverse('note:deletenote', args=[1])
        r = resolve(url)
        self.assertEqual(r.func.view_class, DeleteNoteView)