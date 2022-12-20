from image_handler import Handler
from image_detecting import Detector
from image_source import Source
import tensorflow_hub as hub


source = Source()
for image_url in source.urls:
    downloaded_image_path = Handler.download_and_resize_image(image_url, 1280, 856, True)
    module_handle = "https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1"
    detector = hub.load(module_handle).signatures['default']
    Detector.run_detector(detector, downloaded_image_path)