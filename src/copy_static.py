import os
import shutil
# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# shutil.copy
# shutil.rmtree


def copy_folder(src_path, dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    if not os.path.exists(src_path):
        raise Exception('Source folder not exist')
    for i in os.listdir(src_path):
        src_join_path = os.path.join(src_path,i)
        dst_join_path = os.path.join(dst_path,i)
        print(f" * {src_join_path} -> {dst_join_path}")
        if os.path.isfile(src_join_path):
            shutil.copy(src_join_path,dst_join_path)
        else:
            copy_folder(src_join_path,dst_join_path)
            print(f'copy folder to {dst_path}')
    
    
    
        