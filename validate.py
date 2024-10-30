from PIL import Image

def is_image(file_path):
    result = True
    try:
        im = Image.open(file_path)
    except:
        result = False
    return result