import pathlib
import zipfile
from . import global_var

class container_class:
    def container_method(self):
        directory = pathlib.Path(global_var.build_dir)
        with zipfile.ZipFile(global_var.pack_name + ".mcpack", mode="w") as archive:
            for file_path in directory.rglob("*"):
                archive.write(
                    file_path,
                    arcname=file_path.relative_to(directory)
                )