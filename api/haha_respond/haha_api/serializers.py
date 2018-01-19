from rest_framework import serializers, exceptions
from .models import User, Question, Vote, Choice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    username = serializers.CharField(max_length=64, allow_blank=False, min_length=2)
    email = serializers.CharField(max_length=64, allow_blank=False, min_length=10)

    # password = serializers.CharField(max_length=64, allow_blank=False, min_length=6)

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        # if validated_data.get('password'):
        #     user.set_password(validated_data['password'])
        user.save()
        return user

    def is_valid(self, raise_exception=False):
        super(UserSerializer, self).is_valid()
        if not str(self.validated_data.get('email', '')).endswith('daocloud.io'):
            raise exceptions.ValidationError(detail="Email should endswith daocloud.io ", code=400)
        email = self.validated_data['email']
        if User.objects.filter(email=email).first():
            raise exceptions.ValidationError(detail="Email %s exists" % email, code=409)

        if User.objects.filter(username=self.validated_data['username']).first():
            raise exceptions.ValidationError(detail="Name %s exists" % email, code=409)

        return True


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id', 'question_text', 'category', 'difficulty')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_id', 'choice_text', 'is_right')


class ExamSerializer(serializers.Serializer):
    exam_id = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    current_question_id = serializers.CharField(required=True)
    last_question_id = serializers.CharField(required=True)
    room_id = serializers.CharField(required=True)


class VoteSerializer(serializers.Serializer):
    vote_id = serializers.CharField(read_only=True)
    exam_id = serializers.CharField(required=True)
    choice_id = serializers.CharField(required=True)
    score = serializers.IntegerField(required=True)
