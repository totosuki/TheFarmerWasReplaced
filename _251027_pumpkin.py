SIZE = get_world_size()
WATER_LINE = 0.25

def watering():
	if get_water() <= WATER_LINE:
		use_item(Items.Water)

def main():
	cnt = 0
	for row in range(SIZE):
		for col in range(SIZE):
			watering()

			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
			
			if can_harvest():
				cnt += 1
			
			move(East)
		move(South)
	
	if cnt == SIZE**2:
		harvest()

def initialize():
	clear()
	
	for _ in range(SIZE - 1):
		move(North)
	
	for row in range(SIZE):
		for col in range(SIZE):
			if get_ground_type() == Grounds.Grassland:
				till()
			move(East)
		move(South)