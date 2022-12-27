from PIL import Image
import base64
from io import BytesIO
from . import global_var

class pack_icon_class:
    def pack_icon_method(bg_out,txt_out):
        txt_rgb_color = pack_icon_class.hex_to_rgb(txt_out)
        bg_rgb_color = pack_icon_class.hex_to_rgb(bg_out)

        pack_icon_bytes = base64.b64decode(global_var.pack_icon_base64)
        pack_icon_image = BytesIO(pack_icon_bytes)
        img = Image.open(pack_icon_image)
        img = img.convert("RGB")

        d = img.getdata()
        new_image = []
        for item in d:
            if item[0] in list(range(200, 256)):
                new_image.append(txt_rgb_color)
            else:
                new_image.append(bg_rgb_color)

        img.putdata(new_image)
        img.save(global_var.build_dir + "pack_icon.png")

    def hex_to_rgb(txt_out):
        h = txt_out.strip("#") 
        rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        return rgb