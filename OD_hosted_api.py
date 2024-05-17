##########################################
# Using the api from roboflow
##########################################

!pip install roboflow supervision opencv-python

!curl -o /content/sample_data/my_bulb.jpg https://images.pexels.com/photos/1073054/pexels-photo-1073054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2

from roboflow import Roboflow
import supervision as sv
import cv2

rf = Roboflow(api_key="O1U3fk8wUMAh6hGAxbFU")
project = rf.workspace().project("bulb-detection")
model = project.version(1).model

#img = "/content/sample_data/my_bulb.jpg"
img = "/content/sample_data/var_tubelight.jfif"
result = model.predict(img, confidence=27, overlap=60).json()

labels = [item["class"] for item in result["predictions"]]

detections = sv.Detections.from_roboflow(result)

label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

image = cv2.imread(img)

annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections, labels=labels)

sv.plot_image(image=annotated_image, size=(16, 16))
