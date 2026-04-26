import pygame
import pytmx


def draw_map(surface, tm_data, camera_x, camera_y):
    for layer in tm_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tm_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tm_data.tilewidth - camera_x, y * tm_data.tileheight - camera_y))

