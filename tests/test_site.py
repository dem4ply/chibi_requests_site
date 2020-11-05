#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from chibi_requests_site import Site_paginate_by_url


class Example_site( Site_paginate_by_url ):
    url = 'https://datos.gob.mx/busca/dataset'


class Test_site( unittest.TestCase ):
    def setUp( self ):
        self.site = Example_site()

    def test_by_default_the_page_should_be_1( self ):
        self.assertEqual( self.site.current_page, 1 )
