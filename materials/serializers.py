from rest_framework.fields import SerializerMethodField
from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_youtube_url


class CourseSerializer(serializers.ModelSerializer):
    lessons = SerializerMethodField()
    subscription = SerializerMethodField()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_subscription(self, course):
        owner = self.context['request'].user
        subscription = Subscription.objects.filter(course=course.id, user=owner.id)
        if subscription:
            return True
        return False

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    video = serializers.URLField(validators=[validate_youtube_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons_in_course = SerializerMethodField()
    course = CourseSerializer()

    def get_count_lessons_in_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "count_lessons_in_course",
        )
