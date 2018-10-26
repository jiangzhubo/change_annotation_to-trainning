import os
from PIL import Image
import xml.etree.ElementTree as ET
import sys

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


rootdir = os.getcwd()
CroppedFolder = "Cropped"
Annotation = "Annotation"
if not os.path.exists(CroppedFolder):
    os.makedirs(CroppedFolder)
    print 'Created "/Cropped/" directory'
a = open('retina_detection.csv','w')
for directory in get_immediate_subdirectories(rootdir):	#loop over all dirs
		
			for filename in os.listdir(directory):
				basename =  os.path.splitext(filename)[0]
				try:
				#	import pdb;pdb.set_trace()	
					file = open ( os.path.join( Annotation,directory, basename)+'.xml')
					root = ET.fromstring(file.read())
					file.close()
					xmin = int (root.find('object').find('bndbox').find('xmin').text)
					ymin = int (root.find('object').find('bndbox').find('ymin').text)
					xmax = int (root.find('object').find('bndbox').find('xmax').text)
					ymax = int (root.find('object').find('bndbox').find('ymax').text)
					label = int (root.find('object').find('name').text)
					if os.path.exists(os.path.join(os.getcwd(), directory, basename)+'.jpg'):
					    a.write('{},{},{},{},{},{}\n'.format(os.path.join(os.getcwd(), directory, basename)+'.jpg',xmin,ymin,xmax,ymax,label))	

				except Exception, e:
					#print "Exception encountered at basename " + basename + " with path as " +  os.path.join( Annotation, directory, basename) 
					print "Unexpected error:", str(e)
a.close()
