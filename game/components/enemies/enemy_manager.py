from game.components.enemies.enemy import Enemy



class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        
    def add_enemy(self):
        if len(self.enemies) < 2:  # Agregar 2 enemigos
            enemy_1 = Enemy()
            enemy_2 = Enemy(is_enemy_2=True)
            self.enemies.append(enemy_1)
            self.enemies.append(enemy_2)