#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.movey = -ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.name == 'Enemy3':
            self.rect.centery += self.movey
            if self.rect.top <= 0:
                self.movey -= self.movey * 3 # 1 - 1 * 3 = -2
            if self.rect.bottom >= WIN_HEIGHT:
                self.movey -= self.movey + ENTITY_SPEED[self.name] # 2 - 2 + 1 = +1



    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
