class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initialize a Television object with default values.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Toggle the power status of the television.
        """
        self.__status = not self.__status

    def mute(self):
        """
        Mute or unmute the television if it is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Increment the channel if the television is powered on.
        Loop back to the minimum channel when at the maximum.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        """
        Decrement the channel if the television is powered on.
        Loop back to the maximum channel when at the minimum.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        """
        Increase the volume if the television is powered on and not muted.
        Unmute the television if it is muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Decrease the volume if the television is powered on and not muted.
        Unmute the television if it is muted.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Return a string representation of the television's current state.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
