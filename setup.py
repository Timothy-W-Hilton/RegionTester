try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test if a (lon, lat) point is within a region',
    'author': 'Timothy W. Hilton',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/Timothy-W-Hilton/RegionTester',
    'author_email': 'thilton@ucmerced.edu',
    'version': '0.1',
    'install_requires': ['nose', 'fiona', 'shapely'],
    'packages': ['RegionTester'],
    'scripts': [],
    'name': 'RegionTester'
}

setup(package_dir={'RegionTester': 'RegionTester'},
      package_data={'RegionTester': ['RegionTester/data/*']},

      **config)
