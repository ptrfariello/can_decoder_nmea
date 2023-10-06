from can_decoder_nmea.exceptions.CANDecoderException import CANDecoderException


class DataSizeMismatchException(CANDecoderException):
    def __init__(self):
        super(DataSizeMismatchException, self).__init__()
    
    pass
