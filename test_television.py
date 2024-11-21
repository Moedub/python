import pytest

from television import Television

def test_init():
    tv = Television()
    assert tv._Television__status is False
    assert tv._Television__muted is False
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status is True
    tv.power()
    assert tv._Television__status is False

def test_mute():
    tv = Television()
    tv.mute()
    assert tv._Television__muted is True
    tv.mute()
    assert tv._Television__muted is False

def test_channel_up():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_CHANNEL + 1):
        tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL

    tv.channel_up()
    assert tv._Television__channel == 1

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL

def test_volume_up():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_VOLUME + 1):
        tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME

    tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME

    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == Television.MAX_VOLUME - 1
