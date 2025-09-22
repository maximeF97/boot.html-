from textnode import TextNode, TextType
from HTMLNode import ParentNode, leafNode
from text_to_html import text_node_to_html_node


import os
import shutil

def copy_from_static_to_public():
    source_dir = "static"
    dest_dir = "public"

    # Delete old public/
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    # Recreate public/
    os.makedirs(dest_dir)

    # Copy recursively, preserving structure
    for root, dirs, files in os.walk(source_dir):
        rel_path = os.path.relpath(root, source_dir)
        dest_path = os.path.join(dest_dir, rel_path) if rel_path != "." else dest_dir

        os.makedirs(dest_path, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dest_path, file)
            shutil.copy2(src_file, dst_file)
            print(f"Copied {src_file} → {dst_file}")

def main():
    # run the static copy
    copy_from_static_to_public()

    # optional: show test node like before
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
