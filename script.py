#!/usr/bin/env python

'''
 ' Pin reading test
'''

from farmware_tools import device, app, get_config_value

PKG = 'Read Pin'
PIN_SENSOR = get_config_value(PKG, 'pin_num')

read_pin = device.read_pin(PIN_SENSOR, 'MoistureSensor', 1)
device.log('Read Pin: {}'.format(read_pin))

get_pin = device.get_pin_value(PIN_SENSOR)
device.log('Get Pin: {}'.format(get_pin))
