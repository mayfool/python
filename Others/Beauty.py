import os
import shutil
import sys
import asyncio


class PictureUtil:
    """Windows聚焦文件夹中图片处理工具类"""

    def __init__(self):

            self.user_name = 'forcast1'
            self.destination_dir = 'd:/pictureTest'
            self.source_path = os.path.join(
                'C:/Users/{user_name}'.format(user_name=self.user_name),
                'AppData/Local/Packages',
                'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
            )
            self.original_files = self.get_original_files()

    def get_original_files(self):
        """获取Windows聚焦文件夹中原始图片名"""

        return os.listdir(self.source_path)

    async def copy_picture(self, original_file, destination_file):
        """复制图片到目标路径"""
        if((os.path.getsize(original_file))>100000):
         shutil.copy(original_file, destination_file)

    def just_do_it(self):
        """任务处理"""

        tasks = [self.copy_picture(os.path.join(self.source_path, o),
                                   os.path.join(self.destination_dir, o+'.JPG'))
                 for o in self.original_files]
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asyncio.wait(tasks))
        finally:
            loop.close()
        print('Done!')

print(1)
PICTURE_UTIL = PictureUtil()
PICTURE_UTIL.just_do_it()