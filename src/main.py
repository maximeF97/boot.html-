import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_page
from generate_page import generate_page_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"   # <- GitHub Pages requires docs directory
dir_path_content = "./content"
template_path = "./template.html"


def main():
    # 1. Basepath from CLI args (default "/")
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages...")
    generate_page_recursive(dir_path_content, template_path, dir_path_docs, basepath)


if __name__ == "__main__":
    main()

