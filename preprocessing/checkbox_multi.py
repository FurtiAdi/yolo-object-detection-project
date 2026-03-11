import os
import cv2
import matplotlib.pyplot as plt

# check bounding box of batch of files

# ---------------- CONFIG ----------------
base_path = "dataset/test"  # change to train/test/valid if needed
class_names = ["blue_bottle", "phone", "red_cup"]
images_per_grid = 16  # number of images per grid
# ----------------------------------------

img_dir = os.path.join(base_path, "images")
lbl_dir = os.path.join(base_path, "labels")

# Get all image files
all_images = [f for f in os.listdir(img_dir) if f.lower().endswith((".jpg", ".png"))]

# Split into batches for grids
for i in range(0, len(all_images), images_per_grid):
    batch = all_images[i:i+images_per_grid]
    fig, axes = plt.subplots(4, 4, figsize=(16,16))
    axes = axes.flatten()

    for ax, img_name in zip(axes, batch):
        img_path = os.path.join(img_dir, img_name)
        label_path = os.path.join(lbl_dir, os.path.splitext(img_name)[0] + ".txt")
        img = cv2.imread(img_path)
        if img is None:
            continue
        h, w, _ = img.shape

        # Draw bounding boxes
        if os.path.exists(label_path):
            with open(label_path, "r") as f:
                for line in f:
                    parts = line.split()
                    if len(parts) < 5:
                        color = (255, 0, 0)  # red for error
                        continue
                    cls, x, y, bw, bh = map(float, parts[:5])
                    if cls >= len(class_names):
                        color = (255, 0, 0)  # red for invalid class
                    else:
                        color = (0, 255, 0)
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

                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(img, label, (x1, y1-5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        ax.imshow(img)
        ax.axis("off")
    plt.tight_layout()
    plt.show()