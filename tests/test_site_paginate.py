#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from chibi_requests_site import Site


class Example_site( Site ):
    url = 'https://datos.gob.mx/busca/dataset'


class Test_site( unittest.TestCase ):
    def setUp( self ):
        self.site = Example_site()

    def test_get_should_work( self ):
        response = self.site.get()
        self.assertEqual( response.status_code, 200 )
