'''
* Copyright 2015-2018 European Atomic Energy Community (EURATOM)
*
* Licensed under the EUPL, Version 1.1 or - as soon they
  will be approved by the European Commission - subsequent
  versions of the EUPL (the "Licence");
* You may not use this work except in compliance with the
  Licence.
* You may obtain a copy of the Licence at:
*
* https://joinup.ec.europa.eu/software/page/eupl
*
* Unless required by applicable law or agreed to in
  writing, software distributed under the Licence is
  distributed on an "AS IS" basis,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
  express or implied.
* See the Licence for the specific language governing
  permissions and limitations under the Licence.
'''


"""
CalCam package.
"""

# Calcam version
__version__ = '2.2.0.a1'

# Some stuff will only work if we have VTK.
try:
    import vtk
except ImportError:
    vtk = None

# Note: We have to import the GUI module before anything
# else to make sure the Calcam GUI and Matplotlib are
# using the same version of Qt and will therefore work well
# together.
if vtk:
    from . import gui
    from .cadmodel import CADModel
    from .raycast import raycast_sightlines
    from .gui import start_gui
    from .render import render_cam_view


# Import the top level "public facing" classes & functions
from .calibration import Calibration
from .raycast import RayData
from .pointpairs import PointPairs

from . import gm
from .gm import GeometryMatrix, PoloidalPolyGrid

from . import geometry_matrix



