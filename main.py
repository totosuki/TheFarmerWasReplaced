import _251022_tree
import _251027_pumpkin

mode = 2
stable = _251022_tree
develop = _251027_pumpkin

if __name__ == "__main__":
	if mode == 1:
		stable.initialize()
		while True:
			stable.main()
	if mode == 2:
		develop.initialize()
		while True:
			develop.main()