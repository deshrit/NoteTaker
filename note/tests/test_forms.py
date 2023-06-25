from django.test import SimpleTestCase
from note.forms import TakeNoteForm, UpdateNoteForm


class TestForms(SimpleTestCase):

    def test_takenoteform_valid_data(self):
        form = TakeNoteForm(data={
            'title': 'title1',
            'body': 'body1'
        })
        self.assertTrue(form.is_valid())

    def test_takenoteform_invlid_data(self):
        form = TakeNoteForm(data={
            'title': '',
            'body': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors.__len__(), 1) # body can be empty

    def test_updatenoteform_valid_data(self):
        form = UpdateNoteForm(data={ 
            'title': 'title1',
            'body': 'body1'
        })
        self.assertTrue(form.is_valid())

    def test_updatenoteform_invlid_data(self):
        form = UpdateNoteForm(data={
            'title': '',
            'body': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)