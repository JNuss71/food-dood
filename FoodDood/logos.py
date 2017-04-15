import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
import google.cloud

def getlogo(file_name):

            # Instantiates a client
    vision_client = vision.Client("Gozkdsby")

            # The name of the image file to annotate


            # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
                    content=content)

            # Performs label detection on the image file
    logos = image.detect_logos()

    # print('Logos:')
    for logo in logos:
        return logo.description
        # print(logo.description)
            # return logos[0];


