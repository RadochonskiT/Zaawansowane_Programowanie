import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image as im
from PIL import ImageColor
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
from six.moves.urllib.request import urlopen
from six import BytesIO
import tempfile

class Handler:
  def display_image(image):
      fig = plt.figure(figsize=(20, 15))
      plt.grid(False)
      plt.imshow(image)
      plt.waitforbuttonpress()

  @staticmethod
  def download_and_resize_image(url, new_width=256, new_height=256,
                                  display=False):
      _, filename = tempfile.mkstemp(suffix=".jpg")
      response = urlopen(url)
      image_data = response.read()
      image_data = BytesIO(image_data)
      pil_image = im.open(image_data)
      pil_image = ImageOps.fit(pil_image, (new_width, new_height), im.ANTIALIAS)
      pil_image_rgb = pil_image.convert("RGB")
      pil_image_rgb.save(filename, format="JPEG", quality=90)
      print("Image downloaded to %s." % filename)
      if display:
        Handler.display_image(pil_image)
      return filename

  def load_img(path):
      img = tf.io.read_file(path)
      img = tf.image.decode_jpeg(img, channels=3)
      return img