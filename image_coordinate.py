#-*- coding: utf-8 -*-
import cv2
import os.path
import glob

def im_trim (img): #함수로 만든다
    x = 640; y = 540; #자르고 싶은 지점의 x좌표와 y좌표 지정
    w = 1320; h = 380; #x로부터 width, y로부터 height를 지정
    img_trim = img[y:y+h, x:x+w] #trim한 결과를 img_trim에 담는다
    #cv2.imwrite('org_trim.jpg',img_trim) #org_trim.jpg 라는 이름으로 저장
    return img_trim #필요에 따라 결과물을 리턴

if __name__ == '__main__':
    files = glob.glob('*.jpg') #templates 폴더안에 있는 jpg파일을 모두 읽음

    for file in files:
        org_image = cv2.imread(file) #test.jpg 라는 파일을 읽어온다
        trim_image = im_trim(org_image) #trim_image 변수에 결과물을 넣는다
        filename_ = file
        cv2.imwrite('test/'+file,trim_image) #자른 이미지를 저장한다
