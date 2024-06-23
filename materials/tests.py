from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test')
        self.course = Course.objects.create(name='Тестовый курс')
        self.lesson = Lesson.objects.create(name='Тестовый урок', description='Урок для теста', course=self.course, owner=self.user)
        self.client.force_authenticate(self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lessons-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lessons-create")
        response = self.client.post(url, {
            'name': 'Тестовый урок',
            'description': 'Урок для теста',
            'course': self.course.pk,
        })
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    # def test_lesson_update(self):
    #     url = reverse("materials:lessons-detail", args=(self.lesson.pk,))
    #     response = self.client.put(url, {
    #         'name': 'Тестовый урок',
    #         'description': 'Урок для теста',
    #         'course': self.course.pk,
    #     })
    #     data = response.json()
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         data.get('name'), 'Тестовый урок'
    #     )

    def test_lesson_delete(self):
        url = reverse("materials:lessons-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:lessons-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('count'), 1
        )


class CourseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test')
        self.lesson = Lesson.objects.create(name='Тестовый урок', description='Урок для теста', course=self.course, owner=self.user)
        self.client.force_authenticate(self.user)

    def test_course_retrieve(self):
        url = reverse("materials:course-retrieve", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.course.name)

    def test_course_create(self):
        url = reverse("materials:course-create")
        response = self.client.post(url, {
            'name': 'Тестовый курс',
        })
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse("materials:course-update", args=(self.course.pk,))
        response = self.client.put(url, {
            'name': 'Тестовый курс',
        })
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Тестовый курс'
        )

    def test_course_delete(self):
        url = reverse("materials:course-delete", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    class SubscriptionTestCase(APITestCase):
        def setUp(self) -> None:
            self.client = APIClient()
            self.user = User.objects.create(email='test@test.com', password='12345')
            self.client.force_authenticate(user=self.user)
            self.course = Course.objects.create(name="test", owner=self.user)
            self.subscription = Subscription.objects.create(course=self.course, user=self.user)

        def test_create_subscription(self):
            data = {
                "user": self.user.id,
                "course": self.course.id,
            }

            response = self.client.post(reverse('materials:subs_create'), data=data)

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )
            (self.assertEqual(
                response.json(),
                {'message': 'подписка удалена'}
            ))