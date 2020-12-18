from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from todos.models import Todo, UserPost
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")

    class Meta:
        model = get_user_model()
        exclude = ['user_permissions','groups',]
        read_only_fields = ['last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined',]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password'
                },
            },
        }
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Password not mathc!"})
        else:
            return data
    
    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class UserPasswordSerializer(serializers.ModelSerializer):
    'change the password'
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    old_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")

    class Meta:
        model = get_user_model()
        fields = ['old_password', 'password', 'confirm_password','url',]
        # exclude = ['user_permissions','groups',]
        # read_only_fields = ['last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined',]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password'
                },
            },
        }
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Password not mathc!"})
        else:
            return data
        
    def validate_old_password(self, value):
        if self.context.get('request').user.check_password(value):
            return value
        raise serializers.ValidationError("Old Password wrong!!!")
            
        
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password')).save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, required=True)
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="user-detail")
    
    class Meta:
        model = get_user_model()
        exclude = ['user_permissions','groups',]
        read_only_fields = ['last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined',]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password'
                },
            },
        }
    
    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Password not mathc!"})
        return data
    
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        print("*"*10, validated_data, "*"*10)
        validated_data.pop('password')
        instance = super(UserSerializer, self).update(instance, validated_data)
        print("*"*10, validated_data, "*"*10)
        return instance

class PasswordChangeSerializsr(serializers.ModelSerializer):
    pass

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
    user_name = serializers.StringRelatedField(source='user', many= False, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='userpost-detail',
        lookup_field='slug'
    )
    class Meta:
        model = UserPost
        fields = '__all__'
        # exclude = ['user', ]
        extra_kwargs = {'user': {'read_only': True},}

      
    def create(self, validated_data):
        request = self.context.get("request")
        if not hasattr(validated_data, "user"):
            if request and hasattr(request, "user"):
                validated_data['user'] = request.user
        return super(UserPostSerializer, self).create(validated_data)
