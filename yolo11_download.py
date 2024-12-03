from ultralytics import YOLO
import os
os.chdir('./model')

# Load a model,Export to onnx with simplify
model = YOLO("yolo11n.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolo11s.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolo11m.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)
