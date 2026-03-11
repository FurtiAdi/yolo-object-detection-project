import cv2
import os

# ---------------- CONFIG ----------------
img_path = "dataset_augment/train/images/img_000074.jpg"
lbl_path = "dataset_augment/train/labels/img_000074.txt"
class_names = ["blue_bottle", "phone", "red_cup"]
class_id = 1  # change if you want to edit a different class
# -----------------------------------------

# Load image
img = cv2.imread(img_path)
clone = img.copy() # type: ignore

# Load existing boxes
boxes = []
if os.path.exists(lbl_path):
    with open(lbl_path, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) < 5:
                continue
            cls, x, y, bw, bh = map(float, parts[:5])
            if int(cls) != class_id:
                continue
            h, w, _ = img.shape 
            x_center = int(x * w)
            y_center = int(y * h)
            box_w = int(bw * w)
            box_h = int(bh * h)
            x1 = int(x_center - box_w/2)
            y1 = int(y_center - box_h/2)
            x2 = int(x_center + box_w/2)
            y2 = int(y_center + box_h/2)
            boxes.append([x1, y1, x2, y2])

# Drawing variables
drawing = False
ix, iy = -1, -1

def draw_box(event, x, y, flags, param):
    global ix, iy, drawing, boxes, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img = clone.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), 2)
            for b in boxes:
                cv2.rectangle(img, (b[0], b[1]), (b[2], b[3]), (0,0,255), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x1, y1 = min(ix, x), min(iy, y)
        x2, y2 = max(ix, x), max(iy, y)
        boxes.append([x1, y1, x2, y2])
        img[:] = clone.copy() 
        for b in boxes:
            cv2.rectangle(img, (b[0], b[1]), (b[2], b[3]), (0,0,255), 1) 

cv2.namedWindow("Edit BBox")
cv2.setMouseCallback("Edit BBox", draw_box)

while True:
    cv2.imshow("Edit BBox", img) 
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to exit
        break
    elif key == ord('r'):  # reset boxes
        boxes = []
        img = clone.copy()
    elif key == ord('s'):  # save boxes
        h, w, _ = img.shape 
        with open(lbl_path, "w") as f:
            for b in boxes:
                x_center = ((b[0]+b[2])/2)/w
                y_center = ((b[1]+b[3])/2)/h
                bw = (b[2]-b[0])/w
                bh = (b[3]-b[1])/h
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {bw:.6f} {bh:.6f}\n")
        print("Saved YOLO labels!")

cv2.destroyAllWindows()