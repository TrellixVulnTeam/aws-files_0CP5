from rest_framework import serializers
from .constants import *


class Employee(object):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired,
                 is_best_employee=None, last_name=None
                 ):
        self.employee_id = employee_id
        self.age = age
        self.date_of_joining = date_of_joining
        self.last_logged_in = last_logged_in
        self.salary_in_inr = salary_in_inr
        self.employee_type = employee_type
        self.first_name = first_name
        self.last_name = last_name
        self.is_retired = is_retired
        self.is_best_employee = is_best_employee


class Company(object):
    def __init__(self, name, registration_id):
        self.name = name
        self.registration_id = registration_id


class EmployeeWithCompanyDetails(Employee):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired, company,
                 is_best_employee=None, last_name=None):
        super().__init__(employee_id, age, date_of_joining, last_logged_in,
                         salary_in_inr, employee_type, first_name, is_retired,
                         is_best_employee, last_name)
        self.company = company

class CompanyWithEmployeesDetails(Company):
    def __init__(self, name, registration_id, employees):
        super().__init__(name, registration_id)
        self.employees = employees


class EmployeeSerializer(serializers.Serializer):

    employee_id = serializers.UUIDField()
    age = serializers.IntegerField()
    date_of_joining = serializers.DateField()
    last_logged_in = serializers.DateTimeField()
    salary_in_inr = serializers.FloatField()
    employee_type = serializers.ChoiceField(
        choices = [
            emp_type.value
            for emp_type in EmployeeTypeEnum
            ]
        )
    first_name = serializers.CharField()
    last_name = serializers.CharField(required=False, allow_null=True)
    is_retired = serializers.BooleanField()
    is_best_employee = serializers.NullBooleanField(required=False)

    def create(self, validated_data):
        return Employee(**validated_data)

'''
    def update(self, instance, validated_data):
        instance.employee_id = validated_data.get(
            'employee_id', instance.employee_id)
        instance.age = validated_data.get(
            'age', instance.age)
        instance.date_of_joining = validated_data.get(
            'date_of_joining', instance.date_of_joining)
        instance.last_logged_in = validated_data.get(
            'last_logged_in', instance.last_logged_in)
        instance.salary_in_inr = validated_data.get(
            'salary_in_inr', instance.salary_in_inr)
        instance.employee_type = validated_data.get(
            'employee_type', instance.employee_type)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.is_retired = validated_data.get(
            'is_retired', instance.is_retired)
        instance.is_best_employee = validated_data.get(
            'is_best_employee', instance.is_best_employee)
'''


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField()
    registration_id = serializers.UUIDField()

    def create(self, validated_data):
        return Company(**validated_data)


class EmployeeWithCompanyDetailsSerializer(EmployeeSerializer):

    company = CompanySerializer()

    def create(self, validated_data):
        company_data = validated_data.pop('company')

        company = Company(**company_data)
        employee_with_company = EmployeeWithCompanyDetails(
            company=company, **validated_data
            )
        return employee_with_company


class CompanyWithEmployeeDetailsSerializer(CompanySerializer):

    employees = EmployeeSerializer(many=True)

    def create(self, validated_data):
        employees_data = validated_data.pop('employees')

        employees = [
            Employee(**employee_data) for employee_data in employees_data
        ]
        company_with_employees = CompanyWithEmployeesDetails(
            employees=employees, **validated_data
        )
        return company_with_employees


# Task-1
def serialize_employee_object(employee_object):

    employee_serializer = EmployeeSerializer(employee_object)
    employee_dict = employee_serializer.data
    return employee_dict


# Task-2
def deserialize_data_to_employee_object(employee_data):

    employee_deserialize = EmployeeSerializer(data=employee_data)
    is_valid_data = employee_deserialize.is_valid()
    if is_valid_data:
        return employee_deserialize.save()
    return employee_deserialize.errors


# Task-3
def serialize_list_of_employee_objects(list_of_employee_objects):

    employees_serializer = EmployeeSerializer(
        list_of_employee_objects, many=True)
    employees_dict = employees_serializer.data
    return employees_dict


# Task-4
def deserialize_data_to_list_of_employee_objects(employees_data):

    employees_deserialize = EmployeeSerializer(data=employees_data, many=True)
    is_valid_data = employees_deserialize.is_valid()
    if is_valid_data:
        return employees_deserialize.save()
    return employees_deserialize.errors


# Task-5
def serialize_employee_with_company_object(employee_with_company_object):

    employee_object = EmployeeWithCompanyDetailsSerializer(
        employee_with_company_object
        )
    return employee_object.data


# Task-6
def deserialize_data_to_employee_with_company_object(employee_with_company_data):

    employee_obj = EmployeeWithCompanyDetailsSerializer(
        data=employee_with_company_data
        )
    if employee_obj.is_valid():
        return employee_obj.save()
    return employee_obj.errors


# Task-7
def serialize_company_with_employees_object(company_with_employees_object):

    company_object = CompanyWithEmployeeDetailsSerializer(
        company_with_employees_object
        )
    return company_object.data


# Task-8
def deserialize_data_to_company_with_employees_object(company_with_employees_data):

    company_object = CompanyWithEmployeeDetailsSerializer(
        data=company_with_employees_data
        )
    if company_object.is_valid():
        return company_object.save()
    return company_object.errors


import uuid
from datetime import datetime, date

def create_employee():
    employee = Employee(
        employee_id = uuid.uuid4(),
        age = 20,
        date_of_joining = date.today(),
        last_logged_in = datetime.now(),
        salary_in_inr = 20000,
        employee_type = 'TECHNICIAN',
        first_name = 'Bala',
        last_name = 'Ganga',
        is_retired = False,
        is_best_employee = True
    )
    return employee

def create_company():
    company = Company(
        name = 'hyper',
        registration_id = uuid.uuid4()
    )
    return company

def create_employee_with_company_details():
    employee_with_company = EmployeeWithCompanyDetails(
        employee_id = uuid.uuid4(),
        age = 20,
        date_of_joining = date.today(),
        last_logged_in = datetime.now(),
        salary_in_inr = 20000,
        employee_type = 'TECHNICIAN',
        first_name = 'Bala',
        last_name = 'Ganga',
        is_retired = False,
        is_best_employee = True,
        company = create_company()
    )
    return employee_with_company

def create_company_with_employees_details():
    company_with_employees = CompanyWithEmployeesDetails(
    name = 'bolar',
    registration_id = uuid.uuid4(),
    employees = [create_employee()]
    )
    return company_with_employees

