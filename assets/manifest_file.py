import json
import uuid
from . import global_var

class manifest_class:
    def manifest_method(self):
        json_var ={
            "format_version": 2,
            "header": {
              "description": global_var.pack_description,
              "name": global_var.pack_name,
              "uuid": str(uuid.uuid4()),
              "version": [0, 0, 1],
              "min_engine_version": [ 1, 19, 0 ]
            },
            "modules": [
              {
                "description": "",
                "type": "resources",
                "uuid": str(uuid.uuid4()),
                "version": [0, 0, 1]
              }
            ]
        }

        with open(global_var.build_dir + "manifest.json", "w") as outfile:
            json.dump(json_var, outfile, indent = 4)