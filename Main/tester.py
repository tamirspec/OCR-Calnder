from Main.photo_processor import Image_processor
from Main.create_event import Create_event
from Main.image_reader import Image
from Main import utils

image_path ='/Users/tamirspector/PycharmProjects/OCR/tests/simple.jpg'
image = Image(image_path)
# image.set_color_to_gray()
image.set_size()
# image.show_image()
processor = Image_processor(image.get_image())
description = processor.image_to_string()
date = utils.get_date_from_picture_to_google_format(description)
start_date = date
print(description)
print(start_date)
creator = Create_event(start_date, start_date, description)
creator.create()
# # print(description)
# # start_date = processor.get_format_date()
