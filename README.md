# YOLO Object Detection
## Data Collection
To create our dataset, we collected open-licensed images from several sources, including Pexels, Pixabay, and Google Image Search, as well as a small number of photographs taken by members of the group. The dataset contains three object classes: phone, blue bottle, and red cup. When selecting images, we aimed to maintain a reasonably balanced distribution between the classes in order to avoid bias during training.Totally 387 images are collected.

The images were annotated using Roboflow, where bounding boxes were manually drawn around each object. The annotation work was divided among the group members to speed up the process. After labeling, the dataset was split into training, validation, and test sets using a 70/20/10 ratio 

## Model Training
As an initial step, we trained a preliminary model directly in Roboflow to verify that the dataset and annotations were working correctly. Once we confirmed that the model could detect the objects, we exported the dataset and continued training our models locally using the YOLO framework.
```
model = YOLO("yolov8s.pt")

model.train(
    data="/content/drive/MyDrive/dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    project="/content/drive/MyDrive/yolo_training",
    name="run1",
    augment=True
)
```


## Evaluation and Observations

| Grund Truth | Prediction |
|---------|---------|
| <img width="416" height="1152" alt="image" src="https://github.com/user-attachments/assets/f6b6f448-bb06-4768-ae86-0c5d58128420" />| <img width="416" height="1152" alt="image" src="https://github.com/user-attachments/assets/c05495c9-59b8-4a00-80ab-95941bcbb1d9" />|

| Class       | Images | Instances | Precision (P) | Recall (R) | mAP50 | mAP50-95 |
| ----------- | ------ | --------- | ------------- | ---------- | ----- | -------- |
| All classes | 77     | 140       | 0.850         | 0.604      | 0.710 | 0.540    |
| blue_bottle | 31     | 58        | 0.789         | 0.569      | 0.664 | 0.508    |
| phone       | 31     | 41        | 0.903         | 0.681      | 0.828 | 0.650    |
| red_cup     | 17     | 41        | 0.859         | 0.561      | 0.639 | 0.462    |
> Result by the model trained with YOLOv8s
## Discussion
The trained model was able to detect the three object classes with reasonable accuracy under normal conditions. However, performance varied depending on factors such as lighting, object orientation, and background complexity. In simpler scenes where the objects were clearly visible, the detector performed reliably. In more complex situations, such as cluttered backgrounds or partially occluded objects, detection accuracy decreased.

Overall, the project demonstrates how dataset quality, annotation accuracy, and class balance influence the performance of an object detection model. Further improvements could likely be achieved by increasing the dataset size, improving class balance, and applying additional data augmentation techniques.
