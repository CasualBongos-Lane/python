import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        pass

    def test_power(self):
        pass

    def test_mute(self):
        pass

    def test_channel_up(self):
        pass

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass