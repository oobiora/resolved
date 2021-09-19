from datetime import datetime
from rest_framework import serializers
from .models import Pledge, Action
from accounts.models import User


class ActionSerializer(serializers.ModelSerializer):
    parent_pledge = serializers.PrimaryKeyRelatedField(required=True, queryset=Pledge.objects.all())

    class Meta:
        model = Action
        exclude = ['frequency']
        depth = 1

    def create(self, validated_data):
        action_step = Action.objects.create(**validated_data)
        return action_step

    def update(self, instance, validated_data):
        instance = super(ActionSerializer, self).update(instance, validated_data)
        return instance

class UpdateActionSerializer(serializers.ModelSerializer):
    id = serializers.ModelField(model_field=Action()._meta.get_field('id'), required=True)
    title = serializers.ModelField(model_field=Action()._meta.get_field('title'), required=False)
    serializers.ModelField(model_field=Action()._meta.get_field('unit'), required=False)
    serializers.ModelField(model_field=Action()._meta.get_field('uamount'), required=False)
    parent_pledge = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Action
        exclude = ['frequency']
        depth = 1

    def update(self, instance, validated_data):
        instance = super(ActionSerializer, self).update(instance, validated_data)
        return instance

class PledgeSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all())
    signers = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Pledge
        fields = '__all__'
        depth = 1


    def create(self, validated_data):
        pledge = Pledge.objects.create(**validated_data)
        return pledge
    

class UpdatePledgeSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())
    signers = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    statement = serializers.ModelField(model_field=Pledge()._meta.get_field('statement'), required=False)
    mission = serializers.ModelField(model_field=Pledge()._meta.get_field('mission'), required=False)
    impact = serializers.ModelField(model_field=Pledge()._meta.get_field('impact'), required=False)
    id = serializers.ModelField(model_field=Pledge()._meta.get_field('id'), required=True)
    class Meta:
        model = Pledge
        fields = '__all__'
        depth = 1


    def update(self, instance, validated_data):
        _signers = validated_data.pop('signers', False)
        instance = super(UpdatePledgeSerializer, self).update(instance, validated_data)
        if _signers:
            instance.signers.add(_signers)
        instance.save()

        return instance



