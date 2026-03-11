import os


# rename all the image files "img_00001.jpg" and label files with "img_00001.txt"
base_path = "dataset"
splits = ["train", "valid", "test"]

counter = 1

for split in splits:
    img_dir = os.path.join(base_path, split, "images")
    lbl_dir = os.path.join(base_path, split, "labels")

    images = sorted(os.listdir(img_dir))

    for img in images:
        img_path = os.path.join(img_dir, img)
        name, ext = os.path.splitext(img)

        label_file = name + ".txt"
        lbl_path = os.path.join(lbl_dir, label_file)

        new_name = f"img_{counter:06d}"

        new_img = os.path.join(img_dir, new_name + ext)
        new_lbl = os.path.join(lbl_dir, new_name + ".txt")

        os.rename(img_path, new_img)

        if os.path.exists(lbl_path):
            os.rename(lbl_path, new_lbl)

        counter += 1