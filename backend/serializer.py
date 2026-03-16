from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Register
from .models import Posts,Comments,Likes,Follow



class Register_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','email','password']

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)


# _______________________ Social Media APi ______________________
class comments_serilizer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comments
        fields='__all__'

class posts_serilizer(serializers.ModelSerializer):
    author=serializers.StringRelatedField(read_only=True)
    comments=comments_serilizer(read_only=True,many=True)
    likes_count=serializers.IntegerField(source='likes.count',read_only=True)

    class Meta:
        model=Posts
        fields=['id','author','content','created_at','comments','likes_count']
        
class likes_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields='__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        post = attrs.get('post')
        if Likes.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError("You have already liked this post.")
        return attrs
    
class follow_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields='__all__'

    def validate(self, attrs):
        follower = self.context['request'].user
        following = attrs.get('following')
        if follower == following:
            raise serializers.ValidationError("You cannot follow yourself.")
        if Follow.objects.filter(follower=follower, following=following).exists():
            raise serializers.ValidationError("You are already following this user.")
        return attrs
