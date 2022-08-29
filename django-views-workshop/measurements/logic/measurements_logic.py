from datetime import datetime
from ..models import Measurement
from variables.logic.variables_logic import get_variable


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement


def create_measurement(measurement):
    measurement = Measurement(variable=get_variable(measurement["variable"]),
                              value=measurement["value"],
                              unit=measurement["unit"],
                              place=measurement["place"],
                              dateTime= datetime.strptime(measurement["dateTime"], "%Y-%m-%d")
                              )
    measurement.save()
    return measurement


def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.variable = get_variable(new_measurement["variable"])
    measurement.value = new_measurement["value"]
    measurement.unit = new_measurement["unit"]
    measurement.place = new_measurement["place"]
    measurement.dateTime = datetime.strptime(new_measurement["dateTime"], "%Y-%m-%d")
    measurement.save()
    return measurement


def delete_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    measurement.delete()
    return measurement
