import pygame
import os
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TILE_TYPES, ASSET_PATHS
from map import GameMap

def load_tile_assets():
    assets = {}
    tile_path = ASSET_PATHS['tiles']
    for terrain in TILE_TYPES:
        image_path = os.path.join(tile_path, f"{terrain}.png")
        assets[terrain] = pygame.image.load(image_path).convert()
    return assets

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Civilization-Lite")
    clock = pygame.time.Clock()

    assets = load_tile_assets()
    game_map = GameMap()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                tile_x, tile_y = game_map.world_to_tile_coords(x, y)
                print(f"Clicked tile: ({tile_x}, {tile_y})")

        screen.fill((0, 0, 0))
        game_map.draw(screen, assets)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()