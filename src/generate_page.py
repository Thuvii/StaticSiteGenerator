import os
from src.markdown_block import markdown_to_html_node,extract_title
from pathlib import Path

def generate_page(src_path, template_path, dst_path,basepath="/"):
    print(f"Generating page from {src_path} to {dst_path} using {template_path}")
    with open(src_path) as f:       
        md = f.read()
        f.close()
    with open(template_path) as f:
        template = f.read()
        f.close()
    htmlnode = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    page = template.replace("{{ Title }}",title)
    page = page.replace("{{ Content }}", htmlnode)
    page = page.replace("href=\"/", f"href=\"{basepath}")
    page = page.replace("src=\"/", f"src=\"{basepath}")
    dir_path = os.path.dirname(dst_path)
    if dir_path !="":   
        os.makedirs(dir_path,exist_ok=True)
    with open(dst_path,'w') as f:
        f.write(page)
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path,basepath="/"):
    for item in os.listdir(dir_path_content):
        path_item = os.path.join(dir_path_content,item)
        if os.path.isfile(path_item) and item.endswith(".md"):
            path_item_public = Path(dest_dir_path,'index.html')
            generate_page(path_item,template_path, path_item_public,basepath)
        elif os.path.isdir(path_item):
            path_item_public = os.path.join(dest_dir_path,item)
            generate_page_recursive( path_item,template_path,path_item_public,basepath)

        
    