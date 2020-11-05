import time
import requests
from chibi.snippet.func import retry_on_exception
from chibi_requests import Chibi_url
import logging


logger = logging.getLogger( 'chibi_request_site.site' )


class Site:
    url = None

    def __init__( self, url=None, *args, parent=None, **kw ):
        if url is None:
            url = self.url
        if not isinstance( url, Chibi_url ):
            url = Chibi_url( url.strip() )

        self.url = url
        self.urls = []
        self.processing_order = []
        self.parent = parent

        for k, v in kw.items():
            setattr( self, k, v )

    @property
    def info( self ):
        try:
            return self._info
        except AttributeError:
            self._info = self.parse_info()
            return self._info

    @property
    def soup( self ):
        try:
            return self._response.native
        except AttributeError:
            self.load()
            return self._response.native

    def load( self ):
        response = self.get()
        self._response = response

    def parse_info( self ):
        raise NotImplementedError(
            "no implementada la funcion de parseo de info" )

    def __del__( self ):
        if hasattr( self, '_session' ) and not self.parent:
            logger.info( f"cerrando session de '{self!r}'" )
            self.session.close()
        if hasattr( self, '_firefox' ):
            logger.info( "cerrando firefox" )
            self.firefox.quit()

    @property
    def session( self ):
        try:
            return self._session
        except AttributeError:
            if self.parent is None:
                self.build_session()
            else:
                self._session = self.parent.session
            return self._session

    @property
    def user_agent( self ):
        return self.session.headers[ 'User-Agent' ]

    @user_agent.setter
    def user_agent( self, value ):
        self.session.headers[ 'User-Agent' ] = value

    def build_session( self ):
        self._session = requests.session()
        self._session.headers.update( {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/56.0.2924.87 Safari/537.36',
        } )

    def wait( self, seconds=1 ):
        time.sleep( seconds )

    @property
    def cookies( self ):
        if self.parent:
            return self.parent.cookies
        try:
            return self._cookies
        except AttributeError:
            return None

    @cookies.setter
    def cookies( self, value ):
        if self.parent:
            self.parent.cookies = value
        else:
            self._cookies = {
                cookie[ 'name' ]: cookie[ 'value' ] for cookie in value }
            self.session.cookies.clear()
            for k, v in self._cookies.items():
                self.session.cookies.set( k, v )

    @retry_on_exception
    def get( self, *args, url=None, delay=1, **kw ):
        if url is None:
            url = self.url
        url.session = self.session
        response = url.get()
        if not self.response_is_ok( response ):
            time.sleep( delay )
            raise Exception( 'retry because the response is not ok' )
        return response

    def response_is_ok( self, response ):
        return response.ok

    @property
    def metadata( self ):
        try:
            return self._metadata
        except AttributeError:
            self._metadata = self.parse_metadata()
            return self._metadata

    def parse_metadata( self ):
        raise NotImplementedError(
            "no implementada la funcion de parseo de metadata" )

    def download( self, path ):
        raise NotImplementedError(
            "no implementada la funcion de download" )
