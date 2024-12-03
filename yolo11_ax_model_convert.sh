#!/bin/bash

# ログファイルの設定
LOG_FILE="build_$(date +%Y%m%d_%H%M%S).log"
exec 1> >(tee -a "$LOG_FILE")
exec 2> >(tee -a "$LOG_FILE" >&2)

echo "Build process started at $(date)"

# モデルビルド関数
build_model() {
    local input=$1
    local output=$2
    local config=$3
    
    echo "Building model: $input"
    pulsar2 build --input "$input" --output_dir output --config "$config" --target_hardware AX620E
    if [ $? -eq 0 ]; then
        cp output/compiled.axmodel "$output"
        echo "Successfully built and copied to $output"
    else
        echo "Error building model $input" >&2
        return 1
    fi
}

# YOLO検出モデル
build_model "model/yolo11m-cut.onnx" "model/yolo11m.axmodel" "config/yolo11-config.json"
build_model "model/yolo11s-cut.onnx" "model/yolo11s.axmodel" "config/yolo11-config.json"
build_model "model/yolo11n-cut.onnx" "model/yolo11n.axmodel" "config/yolo11-config.json"

# YOLOポーズ推定モデル
build_model "model/yolo11m-pose-cut.onnx" "model/yolo11m-pose.axmodel" "config/yolo11-pose_config.json"
build_model "model/yolo11s-pose-cut.onnx" "model/yolo11s-pose.axmodel" "config/yolo11-pose_config.json"
build_model "model/yolo11n-pose-cut.onnx" "model/yolo11n-pose.axmodel" "config/yolo11-pose_config.json"

# YOLO セグメンテーションモデル
build_model "model/yolo11m-seg-cut.onnx" "model/yolo11m-seg.axmodel" "config/yolo11-seg_config.json"
build_model "model/yolo11s-seg-cut.onnx" "model/yolo11s-seg.axmodel" "config/yolo11-seg_config.json"
build_model "model/yolo11n-seg-cut.onnx" "model/yolo11n-seg.axmodel" "config/yolo11-seg_config.json"

echo "Build process completed at $(date)"