import random
import os


class Controllers:

    class File:

        @classmethod
        def file_name_ext_getter(cls, filepath):
            basename = os.path.basename(filepath)
            return os.path.splitext(basename)

        @classmethod
        def file_name_creator(cls, instance_id, tolerans: tuple = (1000000, 9999999)):
            rand: list = list(str(random.randint(tolerans[0], tolerans[1])))
            print(rand)
            rand[(len(rand) // 2)] = instance_id
            return "".join(rand)[:len(str(tolerans[1]))]

    class Image:

        @classmethod
        def img_renamer(cls, instance, file):
            img_name, img_ext = Controllers.File.file_name_ext_getter(file)
            new_img_name = f"{Controllers.File.file_name_creator(instance.id)}{img_ext}"
            return f"images/cache/{new_img_name}"