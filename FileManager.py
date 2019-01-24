class FileManager(object):
    """This is a class of managing the input plain file.
    """
    
    def __init__(self, input_file_path, url_chunk_size):
        """This is a constructor for class FileManager.

        Args:
            input_file_path: Path of the input file.
            url_chunk_size: Size of the chunk of URLs used to download once.
        """
        
        self.input_file_path = input_file_path
        self.url_chunk_size = url_chunk_size

    def fetch_url(self, input_file):
        """This is a function of reading image URLs in the plain text according to the chunk.

        Args:
            input_file: Input file object.

        Returns:
            Return a generator.
        """
        
        urls = []
        while True:
            url = input_file.readline().strip()
            if not url:
                if len(urls) != 0:
                    yield urls
                break
            
            urls.append(url)
            if len(urls) == self.url_chunk_size:
                yield urls
                urls = []

    def get_image_url(self):
        """This is a function of getting image URLs.

        Returns:
            Return a URL generator.

        Raises:
            IOError: File IO error.
        """
        
        try:
            image_url_file = open(self.input_file_path, "r")
            url_generator = self.fetch_url(image_url_file)
            return url_generator
        except IOError as error:
            print(error)
            return None
