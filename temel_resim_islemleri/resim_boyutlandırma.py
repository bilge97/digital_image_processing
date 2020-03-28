import cv2

def main() :
    img = cv2.imread('cicek.png')
    ekran_cozunurluk = 1280, 720
    skala_genislik = ekran_cozunurluk[0]/img.shape[1] #genişlik skalası
    skala_yukseklik = ekran_cozunurluk[1]/img.shape[0] #yukseklik
    skala = min(skala_genislik , skala_yukseklik)

    pencere_genislik = int(img.shape[1] * skala)
    pencere_yukseklik = int(img.shape[0] * skala)

    cv2.namedWindow('Boyutlanabilir Pencere' , cv2.WINDOW_NORMAL) #sizable olmasını sağlar
    cv2.resizeWindow('Boyutlanabilir Pencere' , pencere_genislik , pencere_yukseklik )

    cv2.imshow('Boyutlanabilir Pencere' , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()