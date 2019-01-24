import asyncio
from FileManager import FileManager
from DownloadManager import DownloadManager
import sys


INPUT_FILE_PATH = sys.argv[1]  # Input plain file path argument
OUTPUT_DIRECTORY_PATH = '/images'  # Directory of output images
NUM_OF_SEMAPHORE = 5  # The number of semaphores
URL_CHUNK_SIZE = 10  # The chunk containing the number of URLs to download once


if __name__ == '__main__':
    fileManager = FileManager(INPUT_FILE_PATH, URL_CHUNK_SIZE)
    downloadManager = DownloadManager(OUTPUT_DIRECTORY_PATH, NUM_OF_SEMAPHORE)
    loop = asyncio.get_event_loop()

    url_generator = fileManager.get_image_url()
    if url_generator is not None:
        for urls in url_generator:
            tasks = [downloadManager.download(url) for url in urls]
            loop.run_until_complete(asyncio.wait(tasks))

    loop.close()
