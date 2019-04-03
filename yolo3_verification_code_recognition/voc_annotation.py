import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2018', 'train'), ('2018', 'val')]

classes = ["handwriting_chinese"]


def convert_annotation(year, image_id, list_file):
    in_file = open(wd + '/VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
            print("失败")
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = 'C:/Users/Administrator/Desktop/data'
yolo3_path = 'C:/Users/Administrator/Desktop/deep_learning/keras-yolo3'

for year, image_set in sets:
    image_ids = open(wd + '/VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open(yolo3_path +'/%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

