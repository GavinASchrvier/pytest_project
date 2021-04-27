from unittest.mock import Mock

from racecar import Alarm
from sensor import Sensor


def test_alarm_off_buy_default():
    alarm = Alarm()
    assert not alarm.is_alarm_on


class StubSensor:
    def sample_pressure(self):
        return 5

# stub = a minimal class that implements the method(s) of the class
# called upon by the class you're actually trying to test

def test_low_pressure_activates_alarm():
    alarm = Alarm(sensor=StubSensor())
    alarm.check()
    assert alarm.is_alarm_on

# Import Mock framework; passing class to Mock will let us
# set things like return values to that class's methods etc (like sample_pressure())
def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 20
    alarm = Alarm(stub_sensor)
    # When 'check' happens, it will run into the stub_sensor's predefined
    # return value
    alarm.check()
    assert not alarm.is_alarm_on
