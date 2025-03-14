from constants import GRAVITY, JUMP_HEIGHT, PLAYER_SPEED

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

        
        if not self.collisions['down']:
            self.Yvelocity = min(10, self.Yvelocity + GRAVITY)
        else:
            self.Yvelocity = 0
            
        self.animation.update()
        
    def render(self, surf, offset=(0, 0)):
        # Get the original image
        original_img = self.animation.img()
        # Rotate the image around its center
        rotated_img = pygame.transform.rotate(original_img, -self.deg)
        # Get the rectangle of the rotated image
        rotated_rect = rotated_img.get_rect(center=(self.pos[0] + self.size[0] // 2 - offset[0],
                                                self.pos[1] + self.size[1] // 2 - offset[1]))
        # Draw the rotated image
        surf.blit(rotated_img, rotated_rect)



class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0
        self.jump_speed = JUMP_HEIGHT  # Use the constant from constants.py
        self.rotation_speed = 5  # Increased from 3 to make rotation faster
        self.total_rotation = 0  # Track total rotation during a jump
        
    def update(self, tilemap):
        # Always move at constant speed
        movement = (PLAYER_SPEED, 0)
        
        # Apply gravity
        self.Yvelocity += GRAVITY
        
        # Call parent update with our constant movement
        super().update(tilemap, movement=movement)
        
        self.air_time += 1
        
        # Check if we just landed
        just_landed = False
        if self.collisions['down']:
            if self.air_time > 4:  # We were in the air but now we're not
                just_landed = True
            self.air_time = 0
            
        self.grounded = self.air_time <= 4
        
        # Handle jumping and rotation
        if not self.grounded:
            self.set_action('jump')
            
            # Calculate rotation to complete 360 degrees during jump
            if self.Yvelocity < 0:  # First half of jump (going up)
                target_rotation = 180
            else:  # Second half of jump (falling down)
                target_rotation = 360
                
            # Smoothly rotate toward target but faster
            degrees_left = target_rotation - self.total_rotation
            rotation_step = min(self.rotation_speed, degrees_left / 5 + 2)   # Modified for faster rotation
            self.total_rotation += rotation_step
            self.deg += rotation_step
            
        else:
            self.set_action('run')
            # Reset rotation tracking when grounded
            if just_landed:
                self.deg = round(self.deg % 360 / 90) * 90  # Snap to nearest full rotation
                self.total_rotation = 0