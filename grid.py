import pygame
from pygame.math import Vector2
from constants import WHITE, BLACK, GRID_SIZE, CELL_SIZE
import random

class Grid:
  def __init__(self):
    # 辞書でグリッドを管理
    self.grid = {}
    self.ammo_tiles = {}

    for x in range(GRID_SIZE):
      for y in range(GRID_SIZE):
        if (x + y) % 2 == 0:
          self.grid[(x, y)] = WHITE
        else:
          self.grid[(x, y)] = BLACK

        if random.random() < 0.1:
          self.ammo_tiles[(x, y)] = True

  def draw(self, screen):
    # 辞書から各タイル情報を描画
    for (x, y), color in self.grid.items():
      pygame.draw.rect(
          screen, color, (x * CELL_SIZE, y *
                          CELL_SIZE, CELL_SIZE, CELL_SIZE)
      )

    # 弾入りマスの場合はグレーの円を描画
      if (x, y) in self.ammo_tiles:
        center = (x * CELL_SIZE + CELL_SIZE // 2,
                  y * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.circle(screen, (128, 128, 128), center, CELL_SIZE // 4)

  def set_tile_white(self, x, y):
    # マスを白にする
    self.grid[(x, y)] = WHITE

  def set_tile_black(self, x, y):
    # マスを黒にする
    self.grid[(x, y)] = BLACK

  def is_white(self, x, y):
    # 指定したマスが白かどうかを確認
    return self.grid.get((x, y)) == WHITE

  def is_black(self, x, y):
    # 指定したマスが黒かどうかを確認
    return self.grid.get((x, y)) == BLACK

  def spawn_ammo_tile(self):
    x, y = random.randint(
        0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    if self.is_black(x, y):
      if (x, y) not in self.ammo_tiles:
        self.ammo_tiles[(x, y)] = True

  def is_ammo_tile(self, x, y):
    return (x, y) in self.ammo_tiles

  def remove_ammo_tile(self, x, y):
    if (x, y) in self.ammo_tiles:
      del self.ammo_tiles[(x, y)]
