from rest_framework import serializers
from api.models import Employee, Car, History


class HistorySerializer(serializers.ModelSerializer):

    make_model = serializers.SerializerMethodField()
    car_year = serializers.SerializerMethodField()
    worker = serializers.SerializerMethodField()
    car_registration = serializers.SerializerMethodField()

    def get_make_model(self, obj):
        return (f"{obj.car.make} {obj.car.model}")

    def get_car_year(self, obj):
        return obj.car.year

    def get_worker(self, obj):
        return obj.employee.name

    def get_car_registration(self, obj):
        return obj.car.registration

    class Meta:
        model = History
        fields = ('id', 'make_model', 'car_year', 'car_registration', 'repair_log', 'worker' )
