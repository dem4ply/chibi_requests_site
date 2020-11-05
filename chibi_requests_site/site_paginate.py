from .site import Site
from chibi.metaphors import Book


class Site_paginate_by_url( Site ):
    page_url_param = 'page'
    page_size = 1
    page_offset_dict={ 'page': 'page' }

    @property
    def last_page( self ):
        raise NotImplementedError

    @property
    def current_page( self ):
        return int( self.url.params.get( self.page_url_param, 1 ) )

    @property
    def pages( self ):
        book = Book(
            total_elements=self.last_page, page_size=self.page_size,
            page=self.current_page, offset_dict=self.page_offset_dict )
        for page in book:
            url = type( self )( self.url + page, parent=self )
            yield url
