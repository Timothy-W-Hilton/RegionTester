"""module to test whether a (longitude, latitude) pair is within a US State
"""

import os
import fiona
import shapely.geometry
import pkg_resources

class InUSState(object):
    """methods to test if a (longitude, latitude) pair is in a US State
    """

    def __init__(self, shapefile=None):
        """populate shapefile fields

        Fields us_state_shapefile and us_nation_shapefile are
        populated automatically.  If a user-provided shapefile is
        specified in the argument it is placed in self.shapefile.

        ARGS:
        shapefile (string): full path to a shapefile
        """
        self.us_state_shapefile = pkg_resources.resource_filename(
            'RegionTester',
            os.path.join('data', 'cb_2015_us_state_500k', 'cb_2015_us_state_500k.shp'))
        self.us_nation_shapefile = pkg_resources.resource_filename(
            'RegionTester',
            os.path.join('data', 'cb_2015_us_nation_5m', 'cb_2015_us_nation_5m.shp'))
        self.shapefile = shapefile

    def get_state_shape(self, statename):
        """populate self.state_shape

        self.state_shape is a shapely.geometry.polygon.PolygonAdapter
        for the shapefile record for the specified state
        """
        fc = fiona.open(self.us_state_shapefile)

        for i in range(len(fc)):
            if fc[i]['properties']['NAME'] == statename:
                idx = i
        self.state_record = fc[idx]
        self.state_shape = shapely.geometry.asShape(
            self.state_record['geometry'])
        fc.close()

    def point_inside(self, lon, lat):
        """return True if lon, lat is in state, False otherwise
        """
        point = shapely.geometry.Point(lon, lat)
        return self.state_shape.contains(point)
