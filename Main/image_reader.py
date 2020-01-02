from PIL import Image as Im
from PIL import ImageFilter as If

class Image:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Im.open(self.image_path)

    def get_image(self):
        return self.image
    def sharp_image(self):
        self.image = self.image.filter(If.SHARPEN)

    def set_size(self):
        img = self.image
        img = img.resize((3000,3000))
        self.image=img
    def set_color_to_gray(self):
        image_gray = self.image.convert('LA')
        self.image = image_gray

    def set_color_to_light_gray(self):
        image_normal = self.image.convert('1')
        self.image = image_normal

    def show_image(self):
        self.get_image().show()

