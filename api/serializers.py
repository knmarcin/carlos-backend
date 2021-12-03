import datetime
from rest_framework import serializers
from api.models import History, Employee, Car


class HistorySerializer(serializers.ModelSerializer):
    make_model = serializers.SerializerMethodField()
    car_year = serializers.SerializerMethodField()
    worker = serializers.SerializerMethodField()
    car_registration = serializers.SerializerMethodField()
    service_date = serializers.SerializerMethodField()
    days_to_service = serializers.SerializerMethodField()
    car_owner = serializers.SerializerMethodField()
    car_vin = serializers.SerializerMethodField()
    car_id = serializers.SerializerMethodField()

    @staticmethod
    def get_car_id(obj):
        return obj.car.id

    @staticmethod
    def get_car_vin(obj):
        return obj.car.vin_number

    @staticmethod
    def get_make_model(obj):
        return f"{obj.car.make} {obj.car.model}"

    @staticmethod
    def get_car_year(obj):
        return obj.car.year

    @staticmethod
    def get_worker(obj):
        return obj.employee.name

    @staticmethod
    def get_car_registration(obj):
        return obj.car.registration

    @staticmethod
    def get_service_date(obj):
        return obj.car.service_date

    @staticmethod
    def get_days_to_service(obj):
        try:
            new_date = datetime.date(
                obj.car.service_date.year + 1,
                obj.car.service_date.month,
                obj.car.service_date.day)
            return (new_date - datetime.date.today()).days
        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def get_car_owner(obj):
        return obj.car.owner

    class Meta:
        model = History
        fields = ('id',
                  'date_of_repair',
                  'car_owner',
                  'make_model',
                  'car_year',
                  'car_registration',
                  'repair_log',
                  'worker',
                  'service_date',
                  'days_to_service',
                  'car_vin',
                  'car_id')


class CreateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('car', 'employee', 'repair_log')



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ClosestServicesSerializer(serializers.ModelSerializer):
    days_to_service = serializers.SerializerMethodField()
    make_model = serializers.SerializerMethodField()

    @staticmethod
    def get_make_model(obj):
        return f"{obj.make} {obj.model}"

    @staticmethod
    def get_days_to_service(obj):
        try:
            new_date = datetime.date(
                obj.service_date.year,
                obj.service_date.month,
                obj.service_date.day)
            return (new_date - datetime.date.today()).days


        except Exception as e:
            print(e)
            return -1

    class Meta:
        model = Car
        fields = ('service_date',
                  'owner',
                  'registration',
                  'days_to_service',
                  'make_model',
                  'year',
                  'owner_phone_number',
                  'id')

class DashboardSerializer(serializers.Serializer):
    number_of_repairs = serializers.SerializerMethodField()
    number_of_workers = serializers.SerializerMethodField()
    number_of_cars = serializers.SerializerMethodField()
    number_of_repairs_this_month = serializers.SerializerMethodField()
    number_of_repairs_this_year = serializers.SerializerMethodField()

    @staticmethod
    def get_number_of_repairs():
        return History.objects.all().count()

    @staticmethod
    def get_number_of_workers():
        return Employee.objects.all().count()
    @staticmethod
    def get_number_of_cars():
        return Car.objects.all().count()
        pass
    @staticmethod
    def get_number_of_repairs_this_month():
        today = datetime.date.today()
        return History.objects.filter(date_of_repair__year=today.year,
                                      date_of_repair__month=today.month).count()
    @staticmethod
    def get_number_of_repairs_this_year():
        today = datetime.date.today()
        return History.objects.filter(date_of_repair__year=today.year).count()
