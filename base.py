import camera


class base:

    def __init__(self, imageDir, baseXpos, baseYpos, isAllyBase):
        self.image = camera.load_image(imageDir)
        self.x = baseXpos
        self.y = baseYpos
        self.isAllyBase = isAllyBase

    def draw(self):
        if self.isAllyBase:
            self.image.composite_draw(0, 'h', self.x-camera.cameraXCoord, self.y,300,300)
        else:
            self.image.draw(self.x-camera.cameraXCoord, self.y,300,300)
