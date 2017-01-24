pysal\_examples
===============
.. image:: https://travis-ci.org/sjsrey/pysal_examples.svg?branch=master
        :target: https://travis-ci.org/sjsrey/pysal_examples

Example data sets and helper functions for PySAL

This module is pre-alpha and is part of a `refactoring of
PySAL <https://github.com/pysal/pysal/wiki/PEP-13:-Refactor-PySAL-Using-Submodules>`__.

Using ``pysal_examples``
------------------------

::


    In [1]: import pysal_examples

    In [2]: pysal_examples.available()
    Out[2]:
    ['10740',
     'Line',
     'Point',
     'Polygon',
     'Polygon_Holes',
     'arcgis',
     'baltim',
     'book',
     'burkitt',
     'calemp',
     'chicago',
     'columbus',
     'desmith',
     'geodanet',
     'juvenile',
     'mexico',
     'nat',
     'networks',
     'newHaven',
     'nyc_bikes',
     'sacramento2',
     'sids2',
     'snow_maps',
     'south',
     'stl',
     'street_net_pts',
     'taz',
     'us_income',
     'virginia',
     'wmat']

    In [3]: pysal_examples.explain('baltim')
    Out[3]:
    {'description': 'Baltimore house sales prices and hedonics',
     'explanation': ['* baltim.dbf attribute data',
      '* baltim.shp shape file',
      '* baltim.shx spatial index file',
      '* baltim.tri.k12.kwt Kernel weights using a triangular kernel with 12 neares',
      '  neighbors',
      '* baltim_k4.gwt Nearest neighbor weights (4nn)',
      '* baltim_q.gal Queen contiguity file',
      '* baltimore.geojson',
      'Point data, n=211, k= 17.'],
     'name': 'baltim'}

    In [4]: pysal_examples.get_path('baltim.shp')
    Out[4]: '/home/serge/Documents/p/pysal/src/pysal-reorg/pysal-examples/pysal_examples/baltim/baltim.shp'

