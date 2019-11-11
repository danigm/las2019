# main.py
#
# Copyright 2019 Daniel García Moreno
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, GLib

from .window import LasWindow


class Application(Gtk.Application):
    __APP_ID__ = 'net.danigm.las'

    __DBUSIface__ = ('''
    <node>
      <interface name="net.danigm.las">
        <method name="test">
          <arg type="s" direction="out" name="response"/>
        </method>
      </interface>
    </node>
    ''')

    def __init__(self):
        super().__init__(application_id=self.__APP_ID__,
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = LasWindow(application=self)
        win.present()

    def do_dbus_register(self, connection, path):
        introspection_data = Gio.DBusNodeInfo.new_for_xml(self.__DBUSIface__)
        connection.register_object(path,
                                   introspection_data.interfaces[0],
                                   self.handle_method_call,
                                   None)
        return Gtk.Application.do_dbus_register(self, connection, path)

    def handle_method_call(self, connection, sender, object_path,
                           interface_name, method_name, parameters,
                           invocation):
        args = parameters.unpack()
        if not hasattr(self, method_name):
            invocation.return_dbus_error("org.gtk.GDBus.Failed",
                                         "This method is not implemented")
            return

        invocation.return_value(getattr(self, method_name)(*args))

    # DBUS method
    def test(self):
        return GLib.Variant('(s)', ('Test method result', ))


def main(version):
    app = Application()
    return app.run(sys.argv)


class Application2(Application):
    __APP_ID__ = 'net.danigm.las2'

    __DBUSIface__ = ('''
    <node>
      <interface name="net.danigm.las2">
        <method name="test">
          <arg type="s" direction="out" name="response"/>
        </method>
      </interface>
    </node>
    ''')

    def __init__(self):
        super().__init__()

    # DBUS method
    def test(self):
        return GLib.Variant('(s)', ('LAS2 Test method result', ))


def main2(version):
    app = Application2()
    return app.run(sys.argv)
