class Television:
    """
    A class representing the controls for a TV remote
    Also declares four class variables used to set default values throughout the program
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__status: bool = False

    def power(self) -> None:
        '''
        Determines if the TV is on or not,
        determines whether the functions work or not
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False


    def mute(self) -> None:
        '''
        Determines whether the tv is muted or not
        '''
        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self) -> None:
        '''
        This function sets the channel up one and adjusts the chanel variable accordingly
        if the channel is at the maximum, it changes back to the minimum instead
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        This function sets the channel down one and adjusts the chanel variable accordingly
        if the channel is at the minimum, it changes back to the maximum instead
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Changes the volume up one and unmutes the tv.
        If the volume is at max, it stays at max
        '''
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__muted = False
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        '''
        Changes the volume down one and unmutes the tv.
        If the volume is at the minimum, it stays at the minimum
        '''
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__muted = False
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        :return: Returns all the different types of Values in a string format.
        The values return are Power, Channel, Volume
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'