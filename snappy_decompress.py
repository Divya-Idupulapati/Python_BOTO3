#$AUTHOR$:Divya Idupulapati
#$DATE$:06/10/2024
#$VERSION$:1.0
#$LICENSE$:MIT
#$DESCRIPTION$:Decompress .snz files using snappy and read the first 100 lines of each decompressed file
import os
import snappy

# with open(local_snz_path, "rb") as src, open(out_path, "wb") as dst:
        # snappy.stream_decompress(src=src, dst=dst)

local_snz_path = "./"
dst_dir = "./snappy_decompress/"

# if not os.path.exists(dst_dir):
#     os.makedirs(dst_dir)
# for filename in os.listdir(local_snz_path):
#     if filename.endswith(".snz"):
#         out_path = os.path.join(dst_dir, filename[:-4])  # Remove .snz extension
#         with open(os.path.join(local_snz_path, filename), "rb") as src, open(out_path, "wb") as dst:
#             snappy.stream_decompress(src=src, dst=dst)
#         print(f"Decompressed {filename} to {out_path}")

#I want to open notepad using OS module and capture the PID
pid = os.system("notepad.exe")
print(f"Notepad opened with PID: {pid}")

#Want to read each decompressed file and print the first 100 lines
for filename in os.listdir(dst_dir):
    if not filename.endswith(".snz"):
        file_path = os.path.join(dst_dir, filename)
        print(f"First 100 lines of {filename}:")
        with open(file_path, "r") as f:
            for i, line in enumerate(f):
                if i >= 100:
                    break
                print(line.strip())
        print("\n")