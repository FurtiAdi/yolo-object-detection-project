To create our dataset, we collected open-licensed images from several sources, including Pexels, Pixabay, and Google Image Search, as well as a small number of photographs taken by members of the group. The dataset contains three object classes: phone, blue bottle, and red cup. When selecting images, we aimed to maintain a reasonably balanced distribution between the classes in order to avoid bias during training.

The images were annotated using Roboflow, where bounding boxes were manually drawn around each object. The annotation work was divided among the group members to speed up the process. After labeling, the dataset was split into training, validation, and test sets using a 70/20/10 ratio.

Model Training

As an initial step, we trained a preliminary model directly in Roboflow to verify that the dataset and annotations were working correctly. Once we confirmed that the model could detect the objects, we exported the dataset and continued training our models locally using the YOLO framework.

Evaluation and Observations

The trained model was able to detect the three object classes with reasonable accuracy under normal conditions. However, performance varied depending on factors such as lighting, object orientation, and background complexity. In simpler scenes where the objects were clearly visible, the detector performed reliably. In more complex situations, such as cluttered backgrounds or partially occluded objects, detection accuracy decreased.

Overall, the project demonstrates how dataset quality, annotation accuracy, and class balance influence the performance of an object detection model. Further improvements could likely be achieved by increasing the dataset size, improving class balance, and applying additional data augmentation techniques.
