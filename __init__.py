# -*- coding: utf-8 -*-
"""
/***************************************************************************
 taskmanager
                                 A QGIS plugin
 Atribui uma feição a um usuário
                             -------------------
        begin                : 2016-02-02
        copyright            : (C) 2016 by Alex Lopes Pereira
        email                : alex.pereira@sipam.gov.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load taskmanager class from file taskmanager.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .taskmanager import taskmanager
    return taskmanager(iface)
