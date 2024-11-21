class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self.__status = False  # Boolean for TV power status
        self.__muted = False   # Boolean for mute status
        self.__volume = Television.MIN_VOLUME  # Initialize volume to minimum
        self.__channel = Television.MIN_CHANNEL  # Initialize channel to minimum

    def power(self):
        # Toggle the TV power status
        self.__status = not self.__status

    def mute(self):
        # Toggle mute status
        if self.__status:  # Only works if the TV is on
            self.__muted = not self.__muted

    def channel_up(self):
        # Increment channel, wrapping around if maximum is reached
        if self.__status:  # Only works if the TV is on
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        # Decrement channel, wrapping around if minimum is reached
        if self.__status:  # Only works if the TV is on
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        # Increase volume, unmute if muted
        if self.__status:  # Only works if the TV is on
            if self.__muted:
                self.__muted = False  # Unmute when changing volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        # Decrease volume, unmute if muted
        if self.__status:  # Only works if the TV is on
            if self.__muted:
                self.__muted = False  # Unmute when changing volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        # String representation of the TV's state
        status = "On" if self.__status else "Off"
        volume = "Muted" if self.__muted else self.__volume
        return f"Power = {status}, Channel = {self.__channel}, Volume = {volume}"
