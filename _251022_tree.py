SIZE = get_world_size()
GRASS = 2
TREE = 4
CARROT = 6
WATER_LINE = 0.25

def get_grass():
    harvest()

def get_tree():
    harvest()
    plant(Entities.Tree)

def get_carrot():
    harvest()
    plant(Entities.Carrot)

def watering():
    if get_water() <= WATER_LINE:
        use_item(Items.Water)

def main():
    cnt = 0
    for row in range(SIZE):
        for col in range(SIZE):
            cnt += 1

            while not can_harvest():
                pass

            watering()

            if row < TREE and (cnt - row % 2) % 2:
                get_grass()
            elif row < TREE:
                get_tree()
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
            if row < TREE:
                continue
            else:
                till()
                plant(Entities.Carrot)
            move(East)
        move(South)