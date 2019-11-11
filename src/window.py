# window.py
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

from gi.repository import Gtk


@Gtk.Template(resource_path='/net/danigm/las/window.ui')
class LasWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'LasWindow'

    label = Gtk.Template.Child()

    def __init__(self, application):
        super().__init__(application=application)
        self.label.set_text(application.test().unpack()[0])
