import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.Yvelocity = 0
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.grounded = False
        
        self.action = ''
        self.anim_offset = (0 ,0)
        self.deg = 0
        self.set_action('run')
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()
        
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0], movement[1] + self.Yvelocity)
        
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()

        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        
        self.Yvelocity = min(5, self.Yvelocity + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.Yvelocity = 0
            
        self.animation.update()
        
    def render(self, surf, offset=(0, 0)):
        rect = pygame.Rect(self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1], self.size[0], self.size[1])
        #pygame.draw.rect(surf, (255, 0, 0), rect)
        surf.blit(pygame.transform.rotate(self.animation.img(), -self.deg), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))



class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0
    
    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)
        
        self.air_time += 1
        if self.collisions['down']:
            self.air_time = 0
            
        self.grounded = self.air_time <= 4

        if not self.grounded:
            self.set_action('jump')
            self.deg += 5
        else:
            self.set_action('run')
            self.deg = round(self.deg % 360 / 90) * 90
