import asyncio
import aiohttp
import aiofiles


class DownloadManager(object):
    """This class is used for scraping the images.
    """
    
    def __init__(self, output_directory_path, num_of_semaphore):
        """This is a constructor for class DownloadManager.

        Args:
            output_directory_path: Path of the output directory.
            num_of_semaphore: Number of semaphores.
        """
        
        self.semaphore = asyncio.Semaphore(num_of_semaphore)
        self.output_directory_path = output_directory_path

    async def download(self, url):
        """This is an asynchronous function of downloading images by URLs.

        Args:
            url: URL of the image.

        Returns:
            True for success.

        Raises:
            ClientConnectorError: Cannot connect to host.
        """
        
        try:
            async with self.semaphore:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as image:
                        img_data = await image.read()
                        img_path = '/'.join([self.output_directory_path, url.split('/')[-1]])
                        img_file = await aiofiles.open(img_path, 'wb')
                        await img_file.write(img_data)
                        return True
        except Exception as error:
            print(error)
            