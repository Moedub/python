import pytest
from television import Television


class Test:
    def test_init(self):
        """
        Test the initialization of the Television object.
        """
        tv = Television()
        assert tv._Television__status is False
        assert tv._Television__muted is False
        assert tv._Television__volume == Television.MIN_VOLUME
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_power(self):
        """
        Test the power toggle functionality.
        """
        tv = Television()
        tv.power()
        assert tv._Television__status is True
        tv.power()
        assert tv._Television__status is False

    def test_mute(self):
        """
        Test the mute functionality.
        """
        tv = Television()
        tv.power()  # Ensure the TV is on before muting
        tv.mute()
        assert tv._Television__muted is True
        tv.mute()
        assert tv._Television__muted is False

    def test_channel_up(self):
        """
        Test the channel increment functionality.
        """
        tv = Television()
        tv.power()  # Ensure the TV is on before changing channels
        for _ in range(Television.MAX_CHANNEL + 1):
            tv.channel_up()
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_channel_down(self):
        """
        Test the channel decrement functionality.
        """
        tv = Television()
        tv.power()  # Ensure the TV is on before changing channels
        tv.channel_down()
        assert tv._Television__channel == Television.MAX_CHANNEL

    def test_volume_up(self):
        """
        Test the volume increment functionality.
        """
        tv = Television()
        tv.power()  # Ensure the TV is on before changing volume
        for _ in range(Television.MAX_VOLUME + 1):
            tv.volume_up()
        assert tv._Television__volume == Television.MAX_VOLUME

    def test_volume_down(self):
        """
        Test the volume decrement functionality.
        """
        tv = Television()
        tv.power()  # Ensure the TV is on before changing volume
        tv.volume_down()
        assert tv._Television__volume == Television.MIN_VOLUME

        for _ in range(Television.MAX_VOLUME):
            tv.volume_up()
        tv.volume_down()
        assert tv._Television__volume == Television.MAX_VOLUME - 1
