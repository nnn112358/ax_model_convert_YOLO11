# ax_model_convert_YOLO11

# 目的

YOLO11のオブジェクト認識、ポーズ認識、セグメンテーションのモデルを Module-LLM(ax630c)のNPUで動かすために、
axmodelへの変換を行います。


## pulsar2のインストール

@qqc -sanが管理するGoogleDriveからax_pulsar2_3.2_patch1_temp_vlm.tar.gzをダウンロードしてきます。
<https://drive.google.com/drive/folders/10rfQIAm5ktjJ1bRMsHbUanbAplIn3ium>

dockerをインストールし、以下のコマンドでdockerを読み込みます。

```
sudo docker load -i ax_pulsar2_3.2_patch1_temp_vlm.tar.gz
```
Dockerイメージを確認します。
```
$ sudo docker image ls
REPOSITORY                  TAG             IMAGE ID       CREATED         SIZE
pulsar2                     3.2             9a6b9d26f6a1   2 months ago    2.58GB
pulsar2                     temp-58aa62e4   c6ccb211d0bc   4 weeks ago     2.58GB
```

Dockerを起動します。

```
$ sudo docker run -it --net host --rm -v $PWD:/data pulsar2:temp-58aa62e4
 ```

Dockerを終了します。
```
$ exit
 ```

## Ultralyticsのインストール

Pytorchをインストールした後に、Ultralytics をインストールします。
ここでは、CPU環境のPytorchをインストールしています。

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install ultralytics
```



## axモデルへの変換

このリポジトリをダウンロードし、pythonスクリプトを実行します。

```
$ git clone https://github.com/nnn112358/ax_model_convert_YOLO11
$ cd ax_model_convert_YOLO11
```


オブジェクト認識モデルをUltralyticsからダウンロードして、モデルの最終段のカットを行います。
YOLO11のm/s/nサイズをダウンロードします。

```
$ python yolo11_download.py
$ python yolo11_cut-onnx.py
```

セグメンテーション認識モデルをUltralyticsからダウンロードして、モデルの最終段のカットを行います。
YOLO11-segのm/s/nサイズをダウンロードします。

```
$ python yolo11-seg_download.py
$ python yolo11-seg_cut-onnx.py
```

ポーズ認識モデルをUltralyticsからダウンロードして、モデルの最終段のカットを行います。
YOLO11-poseのm/s/nサイズをダウンロードします。

```
$ python yolo11-pose_download.py
$ python yolo11-pose_cut-onnx.py
```

Pulsar2がインストールされている、Dockerを起動します。

```
$ sudo docker run -it --net host --rm -v $PWD:/data pulsar2:temp-58aa62e4
```

Pulsar2のbuildコマンドで、onnxモデルをModule-LLM(ax630c)のNPUに対応するaxモデルに変換します。

```
pulsar2 build --input model/yolo11m-cut.onnx --output_dir output --config config/yolo11-config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11m.axmodel
pulsar2 build --input model/yolo11s-cut.onnx --output_dir output --config config/yolo11-config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11s.axmodel
pulsar2 build --input model/yolo11n-cut.onnx --output_dir output --config config/yolo11-config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11n.axmodel

pulsar2 build --input model/yolo11m-pose-cut.onnx --output_dir output --config config/yolo11-pose_config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11m-pose.axmodel
pulsar2 build --input model/yolo11s-pose-cut.onnx --output_dir output --config config/yolo11-pose_config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11s-pose.axmodel
pulsar2 build --input model/yolo11n-pose-cut.onnx --output_dir output --config config/yolo11-pose_config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11n-pose.axmodel

pulsar2 build --input model/yolo11m-seg-cut.onnx --output_dir output --config config/yolo11-seg_config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11m-seg.axmodel
pulsar2 build --input model/yolo11s-seg-cut.onnx --output_dir output --config config/yolo11-seg_config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11s-seg.axmodel
pulsar2 build --input model/yolo11n-seg-cut.onnx --output_dir output --config config/yolo11-seg_config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolo11n-seg.axmodel
```

モデルが生成できていることを確認します。

```
$ ls model
app.log                yolo11m-seg.onnx       yolo11n-pose.onnx     yolo11n.pt             yolo11s-seg.onnx
yolo11m-cut.onnx       yolo11m-seg.pt         yolo11n-pose.pt       yolo11s-cut.onnx       yolo11s-seg.pt
yolo11m-pose-cut.onnx  yolo11m.axmodel        yolo11n-seg-cut.onnx  yolo11s-pose-cut.onnx  yolo11s.axmodel
yolo11m-pose.axmodel   yolo11m.onnx           yolo11n-seg.axmodel   yolo11s-pose.axmodel   yolo11s.onnx
yolo11m-pose.onnx      yolo11m.pt             yolo11n-seg.onnx      yolo11s-pose.onnx      yolo11s.pt
yolo11m-pose.pt        yolo11n-cut.onnx       yolo11n-seg.pt        yolo11s-pose.pt
yolo11m-seg-cut.onnx   yolo11n-pose-cut.onnx  yolo11n.axmodel       yolo11s-seg-cut.onnx
yolo11m-seg.axmodel    yolo11n-pose.axmodel   yolo11n.onnx          yolo11s-seg.axmodel
```

# 参考

https://pulsar2-docs.readthedocs.io/en/latest/index.html

