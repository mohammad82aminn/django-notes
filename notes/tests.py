from django.test import TestCase
from django.urls import reverse


class NotesListViewTest(TestCase):
    def test_notes_list_view_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_notes_list_view_url_by_name(self):
        response = self.client.get(reverse("notes:list"))
        self.assertEqual(response.status_code, 200)