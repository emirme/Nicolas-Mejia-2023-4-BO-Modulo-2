from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BROAD_SHOT, BROAD_SHOT_TYPE

class BroadShot(PowerUp):
	"""docstring for BroadShot"""
	def __init__(self):
		super().__init__(BROAD_SHOT, BROAD_SHOT_TYPE)