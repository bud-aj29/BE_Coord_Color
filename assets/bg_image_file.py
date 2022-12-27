from PIL import Image
import json
from . import global_var

class bg_image_class:
    def bg_image_method(bg_out):
        img = Image.new('RGB', (1, 1), color = bg_out)
        img.save(global_var.build_dir + "textures/" + global_var.pack_name + ".png")

        json_var ={
            "nineslice_size": 1,
            "base_size": [
              1,
              1
            ]
        }

        with open(global_var.build_dir + "textures/" + global_var.pack_name + ".json", "w") as outfile:
            json.dump(json_var, outfile, indent = 4)