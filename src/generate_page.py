import os
from gencontent import generate_page


def generate_page_recursive(dir_path_content, template_path, dir_path_public):
    

    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                content_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(content_file_path, dir_path_content)
                output_file_path = os.path.join(
                    dir_path_public,
                    os.path.splitext(relative_path)[0] + ".html"
                )
                output_dir = os.path.dirname(output_file_path)
                os.makedirs(output_dir, exist_ok=True)
                generate_page(content_file_path, template_path, output_file_path)