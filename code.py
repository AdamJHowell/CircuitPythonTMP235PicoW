import time

import analogio
import board


# Function to simplify the math of reading the temperature.
def tmp235_temperature_c( analog_in ):
  cur_value = analog_in.value
  print( f"Current raw value: {cur_value}" )
  ref_voltage = analog_in.reference_voltage
  print( f"Current reference voltage: {ref_voltage}" )
  milli_volts = cur_value * (ref_voltage * 1000 / 65535)
  print( f"Current reference millivolts: {milli_volts}" )
  return (milli_volts - 500) / 10


def get_voltage( pin ):
  return (pin.value * 3.3) / 65536


def voltage_to_c( passed_voltage ):
  return_value = (passed_voltage - 0.5) * 100
  return return_value


def c_to_f( value ):
  return value * 1.8 + 32


if __name__ == '__main__':
  # Create TMP235 analog input.
  tmp235_sensor = analogio.AnalogIn( board.GP28 )

  # Loop forever.
  while True:
    # Read the temperature in Celsius.
    temp_C = tmp235_temperature_c( tmp235_sensor )
    voltage = get_voltage( tmp235_sensor )
    print( f"Volts: {voltage}" )
    print( f"TempC: {voltage_to_c( voltage )}" )
    # Print out the value and delay a second before looping again.
    print( f"Reference temperature: {temp_C:.2f} C {c_to_f( temp_C ):.2f} F" )
    print()
    time.sleep( 2.0 )
