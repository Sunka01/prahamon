import pygame
import pytmx


def vykresli_zem(surface, tm_data, camera_x, camera_y):
    for layer in tm_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tm_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tm_data.tilewidth - camera_x, y * tm_data.tileheight - camera_y))


def nacti_hitboxy_mapy(tmx_data):
    hitboxy = []

    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledObjectGroup):
            for obj in layer:
                new_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                hitboxy.append(new_rect)

    return hitboxy

