"""maxiPago python integration"""
# :copyright: (c) 2013 by Stored (www.stored.com.br).
# :license:   BSD, see LICENSE for more details.

VERSION = (1, 0, 0)
__version__ = '.'.join(map(str, VERSION[0:3])) + ''.join(VERSION[3:])
__author__ = 'Stored'
__contact__ = 'contato@stored.com.br'
__docformat__ = 'restructuredtext'
__license__ = 'MIT'


from maxipago.client import Maxipago
