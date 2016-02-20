#!/usr/bin/env python

'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

import numpy as np
import cv2
import ipdb
import os
import cloudimg.settings as settings
def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def crop_faces(img, rects, margin):
    sub_img_ls = []
    for x1, y1, x2, y2 in rects:
        x1 -= margin
        y1 -= margin
        x2 += margin
        y2 += margin

        x0 = (x1+x2)/2
        y0 = (y1+y2)/2
        sub_img = img[y1:y2, x1:x2]
        w,h = x2-x1, y2-y1
        x_range = np.floor(np.linspace(-w/2, w/2, w))
        y_range = np.floor(np.linspace(-h/2, h/2, h))
        xx,yy = np.meshgrid(x_range, y_range)
        rr = np.sqrt(xx**2 + yy**2)
        sel_radius = np.min([w,h])/2
        exclude_area = np.where(rr > sel_radius)
        alpha_channel = 255*np.ones([sub_img.shape[0], sub_img.shape[1]])
        alpha_channel[exclude_area] = 0
        sub_img = np.stack([sub_img[:,:,0], sub_img[:,:,1], sub_img[:,:,2], alpha_channel], axis = -1)
        sub_img_ls.append(sub_img) 
    return sub_img_ls
def detect_one_img(img_path, margin, output_folder):
	ipdb.set_trace()
	cascade = cv2.CascadeClassifier(settings.BASE_DIR + '/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
	img = cv2.imread(img_path)
	rects = detect(img, cascade)
	#Crop face image
	faces = crop_faces(img, rects, margin)
	face_img_paths = []
	dummy, img_file_name_ext = os.path.split(img_path)
	img_file_name, file_ext = os.path.splitext(img_file_name_ext)
	for i in range(len(faces)):
		face_file_name = output_folder + os.sep + img_file_name + "_face" + str(i+1) + file_ext
		cv2.imwrite(face_file_name, faces[i])
		face_img_paths.append(face_file_name)
	return face_img_paths

def detect_batch(img_folder, margin, output_folder): 
    cascade = cv2.CascadeClassifier(settings.BASE_DIR + '/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
    file_names = next(os.walk(img_folder))[2]
    for afile in file_names:
        img = cv2.imread(os.path.join(img_folder, afile))
        rects = detect(img, cascade)
        #Crop face image
        faces = crop_faces(img, rects, margin)
        for i in range(len(faces)):
            file_name, file_ext = os.path.splitext(afile)
            face_file_name = output_folder + "/" + file_name + "_face" + str(i+1) + ".png"
            cv2.imwrite(face_file_name, faces[i])

