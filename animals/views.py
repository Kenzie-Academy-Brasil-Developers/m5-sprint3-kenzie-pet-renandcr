from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from animals.models import Animal
from animals.serializers import AnimalSerializer

class AnimalCreateListView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)


class AnimalListOneUpdateDeleteView(APIView):
    def get(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
        except:
            return Response({"message": "Animal not found"} ,status=status.HTTP_404_NOT_FOUND)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def patch(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
        except:
            return Response({"message": "Animal not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            if(request.data["group"]):
                return Response({"message": "You can not update group property."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except: 
            pass

        try:
            if(request.data["sex"]):
                return Response({"message": "You can not update sex property."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except: 
            pass

        serializer = AnimalSerializer(animal, request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, animal_id):
        animal = Animal.objects.filter(id=animal_id).delete()
        if not bool(animal[0]):
            return Response({"message": "Animal not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)



