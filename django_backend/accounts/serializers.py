from datetime import datetime

from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import User
from services.models import Pledge, Action
# from services.serializers import PledgeSerializer, ActionStepSerializers

class UserSerializer(serializers.ModelSerializer):
    action_steps = serializers.PrimaryKeyRelatedField(many=True, queryset=Action.objects.all(), required=False)
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['language', 'country']
        depth = 1

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        _action = validated_data.pop('action_steps', False)
        instance = super(UserSerializer, self).update(instance, validated_data)
        if _action:
            instance.add(u_action=_action)
            instance.save()

        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    action_steps = serializers.PrimaryKeyRelatedField(many=True, queryset=Action.objects.all(), required=False)
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['language', 'country']
        depth = 1


    def update(self, instance, validated_data):
        _action = validated_data.pop('action_steps', False)
        instance = super(UserSerializer, self).update(instance, validated_data)
        if _action:
            instance.add(u_action=_action)
            instance.save()

        return instance
    
# class UserSerializer(serializers.ModelSerializer):
#     signed_pledge = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Pledge.objects.all(),
#         pk_field=serializers.IntegerField(),
#         allow_null=True
#     )
#     action_steps = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=ActionStep.objects.all(),
#         pk_field=serializers.IntegerField(),
#         allow_null=True
#     )
#     class Meta:
#         model = User
#         exclude = ['language', 'country']
#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#         return user
    
#     def update(self, instance, validated_data):
#         instance = super(UserSerializer, self).update(instance, validated_data)
#         signed_pledge = validated_data.pop('signed_pledge', None)
#         action_steps = validated_data.pop('action_steps', None)
#         if (signed_pledge != None or action_steps != None):
#             pl = Pledge.objects.filter(id__iexact=signed_pledge['id'])
#             if pl.exists():
#                 pledge = pl.first()
#                 instance.action_steps.add(pledge)

#             ac = ActionStep.objects.filter(id__iexact=action_steps['id'])
#             if ac.exists():
#                 action_step = ac.first()
#                 instance.action_steps.add(action_step)


#         return instance