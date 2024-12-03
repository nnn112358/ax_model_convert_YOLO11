from ultralytics import YOLO
import os
os.chdir('./model')

# Load a model,Export to onnx with simplify
model = YOLO("yolo11n-pose.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolo11s-pose.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolo11m-pose.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)
