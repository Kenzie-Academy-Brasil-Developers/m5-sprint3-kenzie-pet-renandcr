from rest_framework import serializers
from .models import Animal
from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer
from groups.models import Group
from characteristics.models import Characteristic

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)


    def create(self, validated_data):
        group_input_data = validated_data.pop("group")
        Characteristics_input_data = validated_data.pop("characteristics")
        
        group_data = Group.objects.get_or_create(**group_input_data) 
        characteristic_list = []
  
        for item in Characteristics_input_data:
            data = Characteristic.objects.get_or_create(**item)
            characteristic_list.append(data[0])
    
        animal = Animal.objects.create(**validated_data, group=group_data[0])

        for item in characteristic_list:
            item.animals.add(animal)

        return animal

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.weight = validated_data.get("weight", instance.weight)

        instance.save()

        return instance






