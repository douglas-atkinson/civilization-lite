import random
import pygame
from config import MAP_WIDTH, MAP_HEIGHT, TILE_SIZE, TILE_TYPES, TILE_LOOKUP, ASSET_PATHS
import os
import csv

class Tile:
    def __init__(self, x, y, terrain):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.unit = None
        self.city = None

    def draw(self, screen, assets):
        image = assets.get(self.terrain)
        if image:
            screen.blit(image, (self.x * TILE_SIZE, self.y * TILE_SIZE))

class GameMap:
    def __init__(self, map_file=None):

        if map_file:
            self.tiles = self.load_map_from_file(map_file)
        else:
            self.tiles = self.generate_random_map()


    def load_map_from_file(self, map_file):
        map_path = ASSET_PATHS['maps']
        map_path_file = os.path.join(map_path, map_file)
        try:
            with open(map_path_file, 'r', newline='') as map_file_data:
                reader = csv.reader(map_file_data)
                tiles = []
                for y, row in enumerate(reader):
                    tile_row = []
                    for x, terrain in enumerate(row):
                        terrain = terrain.strip()
                        try:
                            terrain_id = int(terrain)
                            terrain_name = TILE_LOOKUP[terrain_id]
                            tile_row.append(Tile(x, y, terrain_name))
                        except (ValueError, KeyError):
                            raise ValueError(f"Invalid terrain type '{terrain}' at ({x}, {y})")
                    tiles.append(tile_row)
                return tiles

        except FileNotFoundError:
            print(f"Map file {map_file} not found. Generating random map instead.")
            return self.generate_random_map()
        except Exception as e:
            print(f"An error occurred: {e}")
            return self.generate_random_map()


    def generate_random_map(self):
        tiles = [
            [Tile(x, y, random.choice(TILE_TYPES)) for x in range(MAP_WIDTH)]
            for y in range(MAP_HEIGHT)]
        return tiles

    def draw(self, screen, assets):
        for row in self.tiles:
            for tile in row:
                tile.draw(screen, assets)

    def get_tile(self, x, y):
        if self.is_valid_tile(x, y):
            return self.tiles[y][x]
        return None

    def get_neighbors(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-directional
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid_tile(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def is_valid_tile(self, x, y):
        return 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT

    def move_cost(self, x, y):
        tile = self.get_tile(x, y)
        if tile:
            if tile.terrain == "water":
                return float("inf")  # Impassable for now
            elif tile.terrain == "mountain":
                return 3
            elif tile.terrain == "forest":
                return 2
            else:
                return 1
        return float("inf")

    def world_to_tile_coords(self, pixel_x, pixel_y):
        return pixel_x // TILE_SIZE, pixel_y // TILE_SIZE

    def tile_to_world_coords(self, tile_x, tile_y):
        return tile_x * TILE_SIZE, tile_y * TILE_SIZE

