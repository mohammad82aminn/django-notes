from django.test import TestCase
from django.urls import reverse

from .models import Note


class NotesListViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            author="Hadi",
            text="SAMPLE TEXT",
        )

    def test_notes_list_view_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_notes_list_view_url_by_name(self):
        response = self.client.get(reverse("notes:list"))
        self.assertEqual(response.status_code, 200)

    def test_notes_list_view_content(self):
        response = self.client.get(reverse("notes:list"))
        self.assertContains(response, self.note.text)