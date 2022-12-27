import json
from . import global_var

class hud_class:
    def hud_method(txt_out,alpha_out,font_out,shadow_out):
        rgb_color = hud_class.hex_to_rgb(txt_out)
        json_var ={
            "namespace": "hud",
            "player_position": {
              "alpha": alpha_out,
              "texture": "textures/" + global_var.pack_name
            },
            "player_position/player_position_text": {
              "font_type":  font_out,
              "color":  rgb_color,
              "shadow": shadow_out
            }
        }

        with open(global_var.build_dir + "ui/hud_screen.json", "w") as outfile:
            json.dump(json_var, outfile, indent = 4)

    def hex_to_rgb(txt_out):
        h = txt_out.strip("#") 
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        rgb_float = tuple((rgb[0]/255,rgb[1]/255,rgb[2]/255))
        return rgb_float