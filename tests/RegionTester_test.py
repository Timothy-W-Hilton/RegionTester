import os
import pkg_resources

def setup_method(RegionTester):
    print "SETUP!"
    print "current interpreter: " + sys.executable

def teardown():
    print "TEAR DOWN!"

def test_import1():
    from RegionTester import region_tester

def test_import2():
    from RegionTester.region_tester import InUSState

def test_import3():
    from RegionTester import *

def test_data_present():
    assert pkg_resources.resource_exists('RegionTester',
                                         'data/cb_2015_us_nation_5m/cb_2015_us_nation_5m.shp')
    assert pkg_resources.resource_exists('RegionTester',
                                         'data/cb_2015_us_state_500k/cb_2015_us_state_500k.shp')

def test_cities():
    from RegionTester.region_tester import InUSState

    sanfrancisco = (-122.4194, 37.7749)
    denver = (-104.9841667, 39.7391667)
    sacramento = (-121.4944, 38.5816)

    California = InUSState()
    California.get_state_shape('California')
    Colorado = InUSState()
    Colorado.get_state_shape('Colorado')

    assert California.point_inside(sanfrancisco[0], sanfrancisco[1])
    assert Colorado.point_inside(denver[0], denver[1])

    assert Colorado.point_inside(sanfrancisco[0], sanfrancisco[1]) is False
    assert California.point_inside(denver[0], denver[1]) is False
