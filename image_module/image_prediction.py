import warnings
warnings.simplefilter(action='ignore')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


from .image_to_array import load_image_into_numpy_array as imar
#from .put_fuzzy_in_image import put_fuzzy_in_image as putfuzz
from .put_morpho_in_image import put_morpho_in_image as putmorph
#from fuzzy import check_fuzzy
from morpho import check_morpho
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

PATH_TO_CKPT =  'C:\\Users\\SOHAM\\Desktop\\Detector\\image_module\\trainedModels\\ssd_mobilenet_RoadDamageDetector.pb' 
PATH_TO_LABELS = 'C:\\Users\\SOHAM\\Desktop\\Detector\\image_module\\trainedModels\\crack_label_map.pbtxt'
NUM_CLASSES = 8

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.compat.v1.GraphDef()
  with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')
    
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = {1:{'id':1, 'name':'Crack'},2:{'id':2, 'name':'Crack'},3:{'id':3, 'name':'Crack'},4:{'id':4, 'name':'Crack'},5:{'id':5, 'name':'Crack/Pothole'},6:{'id':6, 'name':'Pothole'},7:{'id':7, 'name':'Others'},8:{'id':8, 'name':'Others'}}

def prediction(image):
    with detection_graph.as_default():
        with tf.compat.v1.Session(graph=detection_graph) as sess:
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            image_np = imar(image)
            image_np_expanded = np.expand_dims(image_np, axis=0)
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            mp = check_morpho(boxes,image_np,scores)
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                min_score_thresh=0.4,
                use_normalized_coordinates=True,
                line_thickness=8)
            image = Image.fromarray(image_np)
            image = putmorph(image,mp)
            image_np = imar(image)
            l = [mp, image_np]
    return l