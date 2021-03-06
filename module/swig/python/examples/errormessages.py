#! /usr/bin/env python

"""
::BOH

Copyright (c) 2005 Peter Kropf. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
::EOH

Turn on connection level error messages and print the address and
type of all sensors on a 1-wire network.
"""


import sys
import ow


def tree( sensor ):
    print '%7s - %s' % ( sensor._type, sensor._path )
    for next in sensor.sensors( ):
        if next._type in [ 'DS2409', ]:
            tree( next )
        else:
            print '%7s - %s' % ( next._type, next._path )


if __name__ == "__main__":
    if len( sys.argv ) == 1:
        print 'usage: errormessages.py u|serial_port_path'
        sys.exit( 1 )
    else:
        # Turn on the level of message to display
        #ow.error_level(ow.error_level.fatal)
        #ow.error_level(ow.error_level.default)
        #ow.error_level(ow.error_level.connect)
        ow.error_level(ow.error_level.call)
        #ow.error_level(ow.error_level.data)
        #ow.error_level(ow.error_level.debug)

        # Set where the messages are to be displayed
        #ow.error_print(ow.error_print.mixed)
        #ow.error_print(ow.error_print.syslog)
        ow.error_print(ow.error_print.stderr)
        #ow.error_print(ow.error_print.suppressed)

        ow.init( sys.argv[ 1 ] )
        tree( ow.Sensor( '/' ) )
