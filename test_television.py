import pytest
from television import Television


class TestTelevision:
    def test_init(self) -> None:
        """
        Test the initialization of the Television object.
        """
        tv: Television = Television()
        assert tv._Television__status is False
        assert tv._Television__muted is False
        assert tv._Television__volume == Television.MIN_VOLUME
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_power(self) -> None:
        """
        Test the power toggle functionality.
        """
        tv: Television = Television()
        tv.power()
        assert tv._Television__status is True
        tv.power()
        assert tv._Television__status is False

    def test_mute(self) -> None:
        """
        Test the mute functionality.
        """
        tv: Television = Television()
        tv.power()
        tv.mute()
        assert tv._Television__muted is True
        tv.mute()
        assert tv._Television__muted is False

    def test_channel_up(self) -> None:
        """
        Test the channel increment functionality.
        """
        tv: Television = Television()
        tv.power()
        for _ in range(Television.MAX_CHANNEL + 1):
            tv.channel_up()
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_channel_down(self) -> None:
        """
        Test the channel decrement functionality.
        """
        tv: Television = Television()
        tv.power()
        tv.channel_down()
        assert tv._Television__channel == Television.MAX_CHANNEL

    def test_volume_up(self) -> None:
        """
        Test the volume increment functionality.
        """
        tv: Television = Television()
        tv.power()
        for _ in range(Television.MAX_VOLUME + 1):
            tv.volume_up()
        assert tv._Television__volume == Television.MAX_VOLUME

    def test_volume_down(self) -> None:
        """
        Test the volume decrement functionality.
        """
        tv: Television = Television()
        tv.power()
        tv.volume_down()
        assert tv._Television__volume == Television.MIN_VOLUME

        for _ in range(Television.MAX_VOLUME):
            tv.volume_up()
        tv.volume_down()
        assert tv._Television__volume == Television.MAX_VOLUME - 1
