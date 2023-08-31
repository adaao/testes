import cv2

im = cv2.imread('/workspaces/testes/Image_cut/img_1.jpg')

print(type(im))

h, w, c = im.shape

print('width:  ', w)
print('height: ', h)
print('channel:', c)