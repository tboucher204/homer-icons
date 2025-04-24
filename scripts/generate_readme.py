#!/usr/bin/python3

from pathlib import Path

current_directory = Path("./png").resolve().parent
print("Current Script Directory:", current_directory)

def generate_img_tag(file):
    return f'<img src="png/{file.name}" alt="{file.stem}" width="50">'

if __name__ == "__main__":
    imgs = sorted(Path("./png").glob("*.png"))
    print("images:", imgs)
    img_tags = [generate_img_tag(x) for x in imgs]

    with open("README.md", "wt", encoding="UTF-8") as f:
        f.write("# Homer Icons\n\n")
        f.write("NOTE: Special thanks to [NX211](https://github.com/NX211/homer-icons) for leading the way.\n\n")
        f.write("[Homer Icons](https://github.com/tboucher204/homer-icons)\n\n")
        f.write(" ".join(img_tags))
        f.write("\n")
