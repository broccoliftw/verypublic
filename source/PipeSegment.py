import pygame

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
	
class PipeSegment():
	def __init__(self,fixed,rotation,image,water,id,water_image):
		self.start_image = image
		self.fixed = fixed
		self.rotation = rotation
		self.image = image
		self.dirty = 1
		self.water = water
		self.id = id
		self.water_image = water_image
	def rotate(self):
		self.image = rot_center(self.start_image,self.rotation)
	def getImage(self):
		if self.water == 1:
			return rot_center(self.water_image,self.rotation)
		else:
			return rot_center(self.start_image,self.rotation)
		