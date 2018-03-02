#!/usr/bin/env python
import sys, pygame, random, os
from square import Square
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (600,600)
dimensions = (rows,columns) = (4,4)
FPS = 60
black = (0,0,0)
#colors taken from https://yeun.github.io/open-color/
colors = [(134,142,150),(250,82,82),(230,73,128),(190,75,219),(121,80,242),(76,110,245),(34,138,230),(21,170,191),(18,184,134),(64,192,87),(130,201,30),(250,176,5),(253,126,20),(233,236,239),(255,236,153),(0,0,0)]

def calculate_xy(pos,puzzle):
	''' calculates which square is the target '''
	w = screen_size[0] / columns
	h = screen_size[1] / rows
	to_return = (int(pos[0]//w),int(pos[1]//h))
	return to_return

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	font = pygame.font.SysFont("comic sans",64)
	clock = pygame.time.Clock()

	puzzle = []
	perfectPuzzle = []
	(w,h) = (screen_size[0]/columns,screen_size[1]/rows)
	for i in range(rows):
		for j in range(columns):
			position = j*rows + i
			color = colors[position]
			puzzle.append(Square(i,j,str(position+1),w,h,color,font))
			perfectPuzzle.append(Square(i,j,str(position+1),w,h,color,font))
	temp = 1000
	while temp > 0:
		randPos = (random.randrange(screen_size[0]), random.randrange(screen_size[1]))
		randomClick = calculate_xy(randPos, puzzle)
		for z in puzzle:
			if (z.position == randomClick):
				if (puzzle[15].check_proximity(randomClick)):
					z.position = puzzle[15].position
					puzzle[15].position = randomClick
		temp -= 1
	while True:
		clock.tick(FPS)
		screen.fill(black)
		if(puzzle != perfectPuzzle):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit(0)
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					clickedSquare = calculate_xy(pos, puzzle)
					for z in puzzle:
						if(z.position == clickedSquare):
							if(puzzle[15].check_proximity(clickedSquare)):
								z.position = puzzle[15].position
								puzzle[15].position = clickedSquare
		else:
			font = pygame.font.SysFont("arial", 64)
			text = "Congratulations! You won! Press Blank Square to Reset"
			f = font.render(text, True, (255, 255, 255))
			(fwidth, fheight) = font.size(text)
			screen.blit(f, (screen_size[0] / 2, screen_size[1] / 2))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit(0)
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					clickedSquare = calculate_xy(pos, puzzle)
					if clickedSquare == (3, 3):
						os.execl(sys.executable, sys.executable, *sys.argv)

		for p in puzzle:
			p.draw_square(pygame.draw,screen)		

		
		pygame.display.flip()

if __name__ == '__main__':
	main()