from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Person


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_person = Person.objects.create(
            profile = testuser1,
            name = 'testuser1',
            bio = 'I am a test user'
        )
        test_person.save()

    def test_person_content(self):
        person = Person.objects.get(id=1)
        actual_name = str(person.name)
        actual_bio = str(person.bio)
        self.assertEqual(actual_name, 'testuser1')
        self.assertEqual(actual_bio, 'I am a test user')