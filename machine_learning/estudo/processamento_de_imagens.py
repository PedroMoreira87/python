# TAREFAS:
# 1. Abrir todas as imagens em uma pasta (todas as imagens de uma pasta)
# 2. Redimensionar o tamanho de todas as imagem (por exemplo, para 600x600)
# 3. Rotacionar toda as imagens em 90, 180 ou 270 graus;
# 4. Transformar as imagens para tons de cinza (grayscale);
# 5. Transformar todas as imagens em array (numpy)
# ORIENTAÇÕES ADICIONAIS:
# 1. Podem trabalhar com as imagens que forem obtidas do vídeo ou com as 4 imagens que estão contidas na pasta.
# Adicionalmente, podem fazer os mesmos experimentos com algum outro conjunto de imagens que desejem.
# 2. Abaixo estão alguns trechos de código que podem ajudar.


from PIL import Image
import os
import glob
import numpy as np

try:
    # creating a folder
    if not os.path.exists('images/resized_images'):
        os.makedirs('images/resized_images')
    if not os.path.exists('images/rotated_images'):
        os.makedirs('images/rotated_images')
    if not os.path.exists('images/grayscale_images'):
        os.makedirs('images/grayscale_images')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

print("\n========== Adicionando imagens a um array e printando seu tamanho ==========\n")
image_list = []
for filename in glob.glob('images/*.jpg'):
    img = Image.open(filename)
    image_list.append(img)

print(image_list)

print("\n========== Transformando todas as imagens em array (numpy) ==========\n")
numpy_list = [np.array(image) for image in image_list]
print(len(numpy_list))

print("\n========== Printando a imagem que está em RBG e verificando seu tamanho ==========\n")
print(numpy_list[0])  # RGB
print(numpy_list[0].shape)
print(image_list[0])

print("\n========== Transformando o tamanho da imagem para 600x600 e salvando em uma pasta ==========\n")
resized_image_list = []
for img in image_list:
    img = img.resize((600, 600))
    resized_image_list.append(img)

for (i, new) in enumerate(resized_image_list):
    new.save('{}{}{}'.format('C:/Users/Pedro/PycharmProjects/machine_learning/ddd/images/resized_images/', i + 1,
                             '.jpg'))

print(image_list[0].size)
print(resized_image_list[0].size)

print("\n========== Rotacionando todas as imagens em 90, 180, 270 e 360 graus ==========\n")
rotated_image_list = []
rotate = 90
for i in range(4):
    for img in image_list:
        img = img.rotate(rotate)
        rotated_image_list.append(img)
    for (j, new) in enumerate(rotated_image_list):
        new.save('{}{}{}'.format('C:/Users/Pedro/PycharmProjects/machine_learning/ddd/images/rotated_images/',
                                 j + 1, '.jpg'))
    rotate += 90

print("\n========== Transformando as imagens para tons de cinza (grayscale) ==========\n")
grayscale_image_list = []
for img in image_list:
    img = img.convert('LA')
    grayscale_image_list.append(img)
for (i, new) in enumerate(grayscale_image_list):
    new.save('{}{}{}'.format('C:/Users/Pedro/PycharmProjects/machine_learning/ddd/images/grayscale_images/', i + 1,
                             '.png'))

