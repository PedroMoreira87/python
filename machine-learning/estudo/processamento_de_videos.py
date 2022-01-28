# TAREFA EXTRA
# 1. Pegar o vídeo "Odalisca E45.mpg" e transformar em uma sequência de imagens
# ORIENTAÇÕES ADICIONAIS:
# 1. Podem trabalhar com as imagens que forem obtidas do vídeo ou com as 4 imagens que estão contidas na pasta.
# Adicionalmente, podem fazer os mesmos experimentos com algum outro conjunto de imagens que desejem.
# 2. Abaixo estão alguns trechos de código que podem ajudar.

# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture('videos/south_park.mp4')

try:
    # creating a folder
    if not os.path.exists('videos/frames'):
        os.makedirs('videos/frames')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while True:

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './videos/frames/' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
