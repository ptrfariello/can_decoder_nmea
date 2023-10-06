from can_decoder_nmea.exceptions import *
from can_decoder_nmea.iterator import IteratorDecoder, DecodedSignal
from can_decoder_nmea.warnings import *

from can_decoder_nmea.Frame import Frame
from can_decoder_nmea.Signal import Signal
from can_decoder_nmea.SignalDB import SignalDB

try:
    from can_decoder_nmea.dataframe import DataFrameDecoder
except ModuleNotFoundError:
    pass

try:
    import warnings

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", category=SyntaxWarning)
        
        from can_decoder_nmea.DBCLoader import load_dbc
except ModuleNotFoundError:
    pass

from ._version import get_versions
__version__ = get_versions()["version"]
del get_versions
