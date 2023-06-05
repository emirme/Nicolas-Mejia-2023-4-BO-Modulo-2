import pygame
import random

from game.utils.constants import DEFAULT_TYPE, SHIELD_TYPE
from game.components.bullets.bullet import Bullet

class BulletManager:
  def __init__(self):
    self.bullets = []
    self.enemy_bullets = []
    self.shooting_time = random.randint(30, 50)
    self.can_shoot = True
    
  def update(self, game):
    for bullet in self.bullets:
      bullet.update(self.bullets)

      for enemy in game.enemy_manager.enemies:
        if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
          game.enemy_manager.enemies.remove(enemy)
          game.score.update()
          self.bullets.remove(bullet)
          break

    for bullet in self.enemy_bullets:
      bullet.update(self.enemy_bullets)

      if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
        self.enemy_bullets.remove(bullet)
        if game.player.power_up_type != SHIELD_TYPE:
          game.death_count.update()
          game.playing = False
          pygame.time.delay(1000)
          break
        

    current_time = pygame.time.get_ticks()
    if current_time > self.shooting_time and self.can_shoot:
      enemy = random.choice(game.enemy_manager.enemies)
      bullet = Bullet(enemy)
      self.enemy_bullets.append(bullet)
      self.can_shoot = False

    if len(self.enemy_bullets) == 0:
      self.can_shoot = True
      self.shooting_time = current_time + random.randint(30, 50)
  
  def draw(self, screen):
    for bullet in self.bullets:
      bullet.draw(screen)

    for bullet in self.enemy_bullets:
      bullet.draw(screen)
      
  def add_bullet(self, bullet):
    if bullet.owner == 'player' and len(self.bullets) < 3:
      self.bullets.append(bullet)
    #elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
      #self.enemy_bullets.append(bullet)
      
  def reset(self):
    self.bullets = []
    self.enemy_bullets = []