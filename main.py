import cv2
import numpy as np
import mahotas

def show_image():
    filtro = 1

    def text(img, texto, cor=(255,0,0)):
        fonte = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)

    while True:
        img = cv2.imread("dados.jpeg")

        if filtro == 1:
            text(img, "Imagem Original",255)
            cv2.imshow('CVMultimidia', img)

        if filtro == 2:
            text(img, "Tons de Cinza",255)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('CVMultimidia', gray)

        if filtro == 3:
            text(img, "Blur",255)
            blur = cv2.blur(img, (7,7))
            cv2.imshow('CVMultimidia', blur)

        if filtro == 4:
            text(img, "Binarização",255)
            ret1, binarization = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            cv2.imshow('CVMultimidia', binarization)

        if filtro == 5:
            text(img, "Bordas",255)
            edges = cv2.Canny(img, 100, 200)
            cv2.imshow('CVMultimidia', edges)



        if filtro == 9:

            #1)Tons de Cinza
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #2)Blur + Tons de Cinza
            blur = cv2.blur(gray, (7,7))
            #cv2.imshow('CVMultimidia', blur)

            #3) Tons de Cinza + Blur + Binarization
            T = mahotas.thresholding.otsu(blur)
            binarization = blur.copy()
            binarization[binarization > T] = 255
            binarization[binarization < 255] = 0
            binarization = cv2.bitwise_not(binarization)
            #cv2.imshow('CVMultimidia',binarization)

            #4)Edges + Tons de Cinza + Blur + Binarization
            edges = cv2.Canny(binarization, 70, 150)
            #cv2.imshow('CVMultimidia', edges)

            #5)Contour + Edge + Tons de Cinza + Blur + Binarizarion
            contours, lx = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            img2 = img.copy()
            cv2.imshow("CVMultimidia", img)
            cv2.drawContours(img2, contours, -1, (255,0,0), 2)
            text(img2, str(len(contours))+ "dados encontrados!")
            cv2.imshow("CVMultimidia",img2)


        ret = cv2.waitKey(1)

        if ret == 27:
            break

        elif ret == -1:
            continue

        elif ret == 49:
            filtro = 1

        elif ret == 50:
            filtro = 2

        elif ret == 51:
            filtro = 3

        elif ret == 52:
            filtro = 4

        elif ret == 53:
            filtro = 5

        elif ret == 57:
            filtro = 9


cv2.destroyAllWindows()


def main():
    show_image()
    return 0


if __name__ == '__main__':
    main()