import _251022_water
import _251022_tree

mode = 2
stable = _251022_water
develop = _251022_tree

if __name__ == "__main__":
	if mode == 1:
		stable.initialize()
		while True:
			stable.main()
	if mode == 2:
		develop.initialize()
		while True:
			develop.main()