import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    
    # Read markdown
    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    # Read template
    with open(template_path, "r") as template_file:
        template = template_file.read()

    # Convert markdown → HTML
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Insert content
    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

   
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    # Write output
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as to_file:
        to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
