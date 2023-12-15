from flask import request, send_file
from models.image import Image
from PIL import Image as PILImage
import io
from utils import findOut

class ImageController():
    def __init__(self, connection, config):
        self.image = Image(connection=connection)
        self.config = config

    def getHostImage(self):
        hostId = request.args['hostId']
        imageRawBinary = self.image.getHostImage(hostId=hostId)[2]


        image = PILImage.open(io.BytesIO(imageRawBinary))
        image.save(f"{self.config.temp_image_processor_path}/send.png")

        return send_file(f"{self.config.temp_image_processor_path}/send.png", mimetype='image/png')

