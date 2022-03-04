import os
import cv2
import argparse


sift =cv2.xfeatures2d.SIFT_create()
BF = cv2.BFMatcher(cv2.NORM_L2)

def load_img(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    return img

def img2descriptors(img):
    keypoints, descriptors = sift.detectAndCompute(img, None)
    return keypoints, descriptors


def is_match(descriptors_template, descriptors_source, min_match=72):
    matches = BF.knnMatch(descriptors_template, descriptors_source, k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.85*n.distance:
            good.append(m)

    match_flag = False
    if len(good) > min_match:
        match_flag = True
    return match_flag


def matching(source_img):
    _, descriptors_source = img2descriptors(source_img)
    template_names_in_img = []
    for i in range(len(template_names)):
        match_flag = is_match(descriptors_templates[i], descriptors_source, min_match=int(no_descriptors_templates[i]*0.2))
        if match_flag == True:
            template_names_in_img.append(template_names[i])
    return template_names_in_img


if __name__=='__main__':

    # Args
    parser = argparse.ArgumentParser()
    parser.add_argument('img_path', type=str, help='image source path')
    args = parser.parse_args()

    # Extracting Features of Templates
    template_names, descriptors_templates, no_descriptors_templates = [], [], []
    template_dir = './templates'
    for template in os.listdir(template_dir):
        template_name = template.split('.')[0]
        template_path = os.path.join(template_dir, template)
        template_img = load_img(template_path)
        _, descriptors_template = img2descriptors(template_img)
        template_names.append(template_name)
        descriptors_templates.append(descriptors_template)
        no_descriptors_templates.append(descriptors_template.shape[0])

    # Matching
    img_source_path = args.img_path
    source_img = load_img(img_source_path)
    template_names_in_img = matching(source_img)
    for i, book_name in enumerate(template_names_in_img):
        print(f'{i}. {book_name}')