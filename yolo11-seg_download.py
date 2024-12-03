from ultralytics import YOLO
import os
os.chdir('./model')

# Load a model,Export to onnx with simplify
model = YOLO("yolo11n-seg.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolo11s-seg.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolo11m-seg.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)
