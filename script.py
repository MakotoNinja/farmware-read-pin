#!/usr/bin/env python

'''
 ' Pin reading test
'''

from farmware_tools import device, app, get_config_value

PKG = 'Read Pin'
PIN_SENSOR = get_config_value(PKG, 'pin_num')

get_pin = device.get_pin_value(PIN_SENSOR)
device.log('Get Pin: {}'.format(get_pin))

read_pin = device.read_pin(PIN_SENSOR, 'Moisture Sensor', 1)
device.log('Read Pin: {}'.format(read_pin))
