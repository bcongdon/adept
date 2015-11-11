from buffalo import utils
from inventory import Inventory
from item import Item
import random
utils.init()

class TestInventory:
	def test_init(self):
		i = Inventory()
		assert len(i.items) == 10
		assert len(i.items[0]) == 3
		assert i.hotbarSelection == 0

	def test_add_item(self):
		i = Inventory()
		t = Item("test")
		i.addItem(t)
		assert i.hotbar[0] == t
		for x in range(100):
			i.addItem(Item(str(random.random())))
		assert i.items[0][0] is not None
		assert i.items[9][2] is not None

	def test_instantiation(self):
		i = Inventory()
		d = Inventory()
		assert i != d
		assert i.hotbar is not d.hotbar
		assert i.items is not d.items

	def test_rem_item(self):
		i = Inventory()
		t = Item("test",quantity=10)
		i.addItem(t)
		assert i.hotbar[0] == t
		i.removeItemQuantity("test",5)
		print i.hotbar[0].quantity
		assert i.hotbar[0].quantity == 5
