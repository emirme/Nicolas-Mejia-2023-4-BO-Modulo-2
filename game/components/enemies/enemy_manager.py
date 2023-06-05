import pygame
import random

from game.components.enemies.enemy import Enemy
from game.components.bullets.bullet import Bullet


class EnemyManager:
  def __init__(self):
    self.enemies = []
    self.shooting_time = random.randint(30, 50)
    self.can_shoot = True
    
  def update(self, game):
    self.add_enemies()

    for enemy in self.enemies:
      enemy.update(self.enemies, game)

      current_time = pygame.time.get_ticks()
      if current_time > self.shooting_time and self.can_shoot:
        enemmy = random.choice(self.enemies)
        bullet = Bullet(enemy)
        game.bullet_manager.add_bullet(bullet)
        self.can_shoot = False

      if len(self.enemies) == 0:
        self.can_shoot = True
        self.shooting_time = current_time + random.randint(30, 50)
  
  def draw(self, screen):
    for enemy in self.enemies:
      enemy.draw(screen)
      
  def add_enemies(self):
    enemy_type = random.randint(1, 2)
    max_enemies = 5  # Número máximo de enemigos
    if len(self.enemies) < max_enemies:
      if enemy_type == 1:
        enemy = Enemy()
      else:
        x_speed = 5
        y_speed = 2
        move_x_for = [50, 120]
        enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)

      self.enemies.append(enemy)
      
  def reset(self):
    self.enemies = []