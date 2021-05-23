
from sklearn.neighbors import kneighbors_graph
from sklearn.cluster import KMeans,spectral_clustering
import copy
import cv2
import numpy as np

class Five_N_Cut:
  
  def __init__(self):
    self.palette = make_palette()
    
  def make_palette(self):
    grey = [128 ,128, 128]
    pink = [255, 0 ,127]
    viola = [255, 0 ,255]
    blue = [0, 0 ,255]
    green = [0, 255 ,127]
    yellow = [255, 255, 0]
    orange = [255, 128, 0]
    red = [255, 0, 0]
    purple = [127, 0 ,255]
    palette = [grey ,pink, viola ,blue ,green ,yellow, orange ,red ,purple]
    return palette
  
  def five_image_NC(self,image_arr): #return five resized imgs (144, 144)
    Ncut_imgs=[]
    original_imgs = []
    for i in range (5):
      res = cv2.resize(image_arr[i+25], dsize=(144, 144), interpolation=cv2.INTER_CUBIC)
      #cv2_imshow(test_imgs_origin[i+25])
      cv2.waitKey(0)
      #cv2_imshow(res)
      cv2.waitKey(0)
      original_imgs.append(res)
      Ncut_imgs.append(np.float32(res.reshape(-1, res.shape[-1])))
    return np.array(Ncut_imgs), np.array(original_imgs)

  def generate_simlarity(self,image):
    np.set_printoptions(threshold=20736)
    graph= kneighbors_graph(image, 5 , mode='connectivity', include_self=False)
    return graph

  def clustering(self,graph):
    labels = spectral_clustering(graph, n_clusters=5, eigen_solver='arpack') #from 0:4
    return labels

  def cloroing_img(self,image_in,labels):
    print("Shape" ,image_in.shape)
    for i in range(labels.shape[0]):
      if labels[i]==0 :
        image_in[i]=self.palette[1]
      if labels[i]==1 :
        image_in[i]=self.palette[1]
      if labels[i]==2 :
        image_in[i]=self.palette[2]
      if labels[i]==3 :
        image_in[i]=self.palette[3]
      if labels[i]==4 :
        image_in[i]=self.palette[4]
    return image_in
