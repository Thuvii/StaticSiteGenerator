from src.textnode import *
from src.inline_markdown import *
from src.markdown_block import *
from src.htmlnode import *
from src.copy_static import *
from src.generate_page import *
import re
import os
import sys
from pathlib import Path

path_content = "./content/"
path_public = "./docs/"
static_path = "./static"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    if os.path.exists(path_public):
        shutil.rmtree(path_public)
    copy_folder("./static","./docs")
    generate_page_recursive(path_content,"template.html",path_public,basepath)
    # print(os.listdir(path_content))
 


if __name__ == "__main__":
    main()
    
    
    
    