import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        #Testing to see if the correct values are get when the tv is on, turned up one and then muted
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        #unmutes the tv
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # turns tv off while unmuted
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'
        # Tests when the tv is off and muted
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        # Testing the see if the channel is changed when the TV is off
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # Test to see if the channel is changed when the tv is turned on
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'
        # test to see what happens when the channel is changed past the max
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'


    def test_channel_down(self):
        # Testing the see if the channel is changed when the TV is off
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        # Test to see if the channel is changed correctly when the tv is turned on and the channel goes past the min
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'
        # test to see if the channel is changed correctly when the tv is turned on
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 2, Volume = 0'

    def test_volume_up(self):
        #Testing to see if the volume is changed when the tv is off
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        #Testing to see if the volume is changed when the power is on
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # Testing to see whether the volume is changed when muted
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'
        #Testing to see what happens past the max
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'



    def test_volume_down(self):
        # Testing to see if the volume is changed when the tv is off
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        """
        Testing to see whether the volume is changed when the power is on
        The volume is first turned up to make sure that the volume down function works
        """
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        # Testing to see whether the volume is changed when muted
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        # Testing to see what happens past the min
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'