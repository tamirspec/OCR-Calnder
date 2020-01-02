from Main.photo_processor import Image_processor
from Main.create_event import Create_event
from Main.image_reader import Image

image_path ='/Users/tamirspector/PycharmProjects/OCR/tests/eminem_show.jpg'
image = Image(image_path)
image.set_color_to_gray()
image.set_size()
processor = Image_processor(image.get_image())
description = processor.image_to_string()
date = processor.get_formated_google_date()
start_date = date
creator = Create_event(start_date, start_date, description)
creator.create()
# # print(description)
# # start_date = processor.get_format_date()
