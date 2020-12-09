from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from todos.models import Todo


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
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
    username = serializers.SlugRelatedField(source='user', many= False, read_only=True, slug_field="username")
    # user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
        # extra_kwargs = {'user': {'read_only': True},}
    
    # def get_user(self, obj):
    #     print(obj)
    #     return getattr(obj, 'user', 12)

    def get_queryset(self):
        return self.request.user.todo_set.all()
