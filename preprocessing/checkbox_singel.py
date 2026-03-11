import cv2
import matplotlib.pyplot as plt

# check if the bounding box is correct on a single image file
img_path = "dataset_augment/train/images/img_000074.jpg"
lbl_path = "dataset_augment/train/labels/img_000074.txt"

class_names = ["blue_bottle","phone","red_cup"]

# Load image
image = cv2.imread(img_path)
h, w, _ = image.shape 

# Read label file
with open(lbl_path, "r") as f:
    for line in f:
        parts = line.split()
        if len(parts) < 5:
            print("Invalid line:", line)
            continue
        cls, x, y, bw, bh = map(float, parts[:5])
        print(cls,x,y,bw,bh)
        cls = int(cls)
        label = class_names[cls] if cls < len(class_names) else str(cls)

        x_center = int(x * w)
        y_center = int(y * h)
        box_w = int(bw * w)
        box_h = int(bh * h)

        x1 = int(x_center - box_w / 2)
        y1 = int(y_center - box_h / 2)
        x2 = int(x_center + box_w / 2)
        y2 = int(y_center + box_h / 2)

        cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2) 
        cv2.putText(image, label, (x1, y1-5), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2) 

# Show image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
plt.figure(figsize=(6,6))
plt.imshow(image)
plt.axis("off")
plt.show()