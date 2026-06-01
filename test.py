import os

label_dir = (
    "/home/ariefminardi/Work/pcd-uts/pickup-dataset/labels"  # ganti sesuai path lo
)

for filename in os.listdir(label_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(label_dir, filename)

        with open(file_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            parts[0] = "1"  # ganti class_id
            new_lines.append(" ".join(parts))

        with open(file_path, "w") as f:
            f.write("\n".join(new_lines))

print("Done ganti semua class_id jadi 1")
