import cv2
from matplotlib import pyplot as plt
from operator import itemgetter, attrgetter, methodcaller
from Imagem import imagem

similaridadeDeImagem = int(input('Informe qual o taxa minima de similaridade desejada a ser aplicado no processo..? ' ))
total = int(input('Informe o total de registros desejados..: ' ))
listasDeImagens = []

count = 0

video_lido = cv2.VideoCapture("Videos/sym.mp4") # video que será usado
template = cv2.imread('imagem/js.jpeg',0) #imagem usada como parametro de comparação no video que to busando

def redim(img, largura): # to passando meu video e um tamanho de 320, img = tem o frame do video
    alt = int(img.shape[0]/img.shape[1]*largura)
    img = cv2.resize(img, (largura, alt), interpolation = cv2.INTER_AREA)
    return img

df = cv2.CascadeClassifier("modelo/haarcascade_frontalface_default.xml")

while True:
    (sucesso, frame) = video_lido.read()
    if sucesso == True:

         frame = redim(frame, 320)
         frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         faces = df.detectMultiScale(frame_pb, scaleFactor = 1.1, minNeighbors=3, minSize=(5,5), flags=cv2.CASCADE_SCALE_IMAGE)
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         methods = ['cv2.TM_CCOEFF_NORMED']
         # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

         for meth in methods:
            img = frame_pb.copy()
            method = eval(meth)
            res = cv2.matchTemplate(img, template, method)
            min_val, similaridade, min_loc, max_loc = cv2.minMaxLoc(res)
            frame_temp = frame.copy()
         count += 1

         imagem.nome = 'Imagem '+str(count)
         imagem.porcentagem = round(similaridade * 100, 2)
         x = imagem.nome,imagem.porcentagem

         if round(similaridade * 100, 2) > similaridadeDeImagem:
             listasDeImagens.append(x)
             plt.show()

         cv2.imshow('Analisando', redim(gray, 640))
         if cv2.waitKey(15) & 0xFF == ord('q'):
            break
    else:
        break
imagem_ordenados =sorted(listasDeImagens, key = itemgetter(1), reverse=True)
i =0
vet =[]

while (i < total):
    imagem = 'imagem/semelhanca' + str(i) + '.jpg'
    vet.append(imagem_ordenados[i])
    i= i+1

print(vet) #imprime apenas as imagens definidas pelo total
#print(imagem_ordenados) #imprime todas as imagens

video_lido.release()

