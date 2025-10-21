SIZE = get_world_size()
GRASS = 2
BUSH = 5
CARROT = 6
WATER_LINE = 0.25

def get_grass():
	harvest()

def get_bush():
	harvest()
	plant(Entities.Bush)

def get_carrot():
	harvest()
	plant(Entities.Carrot)

def watering():
	if get_water() <= WATER_LINE:
		use_item(Items.Water)

def main():

	for row in range(SIZE):
		for col in range(SIZE):
			while not can_harvest():
				pass

			watering()
			
			if row < GRASS:
				get_grass()
			elif row < BUSH:
				get_bush()
			else:
				get_carrot()
			
			move(East)
		move(South)

def initialize():
	clear()
	
	for _ in range(SIZE - 1):
		move(North)
	
	for row in range(SIZE):
		for col in range(SIZE):
			if row < BUSH:
				continue
			else:
				till()
				plant(Entities.Carrot)
			move(East)
		move(South)