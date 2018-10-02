from PIL import Image
img = Image.open('document.jpeg').convert('L')
img.save('greyscale.jpeg')
