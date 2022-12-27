import os
from . import global_var

class folders_class:
    def folders_method(self):
        if not os.path.exists(global_var.build_dir + "textures"):
            os.makedirs(global_var.build_dir + "textures")
        if not os.path.exists(global_var.build_dir + "ui"):
            os.makedirs(global_var.build_dir + "ui")