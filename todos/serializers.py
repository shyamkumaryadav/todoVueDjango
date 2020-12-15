from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from todos.models import Todo, UserPost


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")
    
    class Meta:
        model = User
        exclude = ['user_permissions','groups',]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                },
            },
            'last_login': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'date_joined': {'read_only': True},
        }
    
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Password not mathc!"})
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if validated_data['confirm_password']:
            instance.set_password(validated_data['confirm_password']) 
            instance.save()
        return instance



class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(source='user', many= False, read_only=True, slug_field="id")
    user = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
        # exclude = ['user', ]
        # extra_kwargs = {'user': {'write_only': True},}

      
    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data['user'] = request.user
        # print(validated_data)
        return super(TodoSerializer, self).create(validated_data)

class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(source='user', many= False, read_only=True, slug_field="id")
    user = serializers.StringRelatedField(many=False, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='userpost-detail',
        lookup_field='slug'
    )
    class Meta:
        model = UserPost
        fields = '__all__'
        
        # exclude = ['user', ]
        # extra_kwargs = {'user': {'write_only': True},}

      
    def create(self, validated_data):
        request = self.context.get("request")
        if not hasattr(validated_data, "user"):
            if request and hasattr(request, "user"):
                validated_data['user'] = request.user
        return super(UserPostSerializer, self).create(validated_data)
