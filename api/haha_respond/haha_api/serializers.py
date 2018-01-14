from rest_framework import serializers, exceptions
from .models import User, Question, Vote


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    username = serializers.CharField(max_length=64, allow_blank=False, min_length=2)
    email = serializers.CharField(max_length=64, allow_blank=False, min_length=10)
    password = serializers.CharField(max_length=64, allow_blank=False, min_length=6)

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        if validated_data.get('password'):
            user.set_password(validated_data['password'])
        user.save()
        return user

    def is_valid(self, raise_exception=False):
        super(UserSerializer, self).is_valid()
        if not self.data.get('email', '').endswith('daocloud.io'):
            raise exceptions.ValidationError(detail="Email should endswith daocloud.io ", code=400)

        return True


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'question_text')


class ExamSerializer(serializers.Serializer):
    exam_id = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True)


class VoteSerializer(serializers.Serializer):
    vote_id = serializers.CharField(read_only=True)
    exam = serializers.CharField(required=True)
    user = serializers.CharField(required=True)
    choice = serializers.CharField(required=True)
    question = serializers.CharField(required=True)
    score = serializers.IntegerField(required=True)

    def create(self, validated_data):
        vote = Vote(
            exam_id=validated_data['exam'],
            user_id=validated_data['user'],
            choice_id=validated_data['choice'],
            question_id=validated_data['question'],
            score=validated_data['score']
        )
        vote.save()
        return vote

    def is_valid(self, raise_exception=False):
        super(VoteSerializer, self).is_valid()
        return True
