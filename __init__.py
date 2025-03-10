__title__ = 'shadowamino'
__author__ = 'shadow'
__license__ = 'MIT'
__copyright__ = 'Copyright 2025 shadow'
__version__ = '1.0.0'

from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .lib.util import exceptions, helpers, objects, headers
from .asyncshadow import acm, client, sub_client, socket
from .socket import Callbacks, SocketHandler
from requests import get
from json import loads

__newest__ = loads(get("https://pypi.org/pypi/shadowamino/json").text)["info"]["version"]

if __version__ != __newest__:
    print(f"New version of {__title__} available: {__newest__} (Using {__version__})")
    print("Visit our community - http://aminoapps.com/c/Utaou")
