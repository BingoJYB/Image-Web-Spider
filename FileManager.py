class FileManager(object):
    """
    This is a class of managing the input plain file.
    """
    def __init__(self, input_file_path, url_chunk_size):
        """
        This is a constructor for class FileManager.

        Args:
            input_file_path: The path of the input file.
            url_chunk_size: The size of the chunk of URLs used to download once.
        """
        self.input_file_path = input_file_path
        self.url_chunk_size = url_chunk_size

    def read_file(self, input_file):
        """
        This is a function of reading image URLs in the plain text by the chunk.

        Args:
            input_file: This is the input file object.

        Returns:
            Return a generator.
        """
        lines = []
        while True:
            line = input_file.readline().strip()
            if not line:
                if len(lines) != 0:
                    yield lines
                break
            
            lines.append(line)
            if len(lines) == self.url_chunk_size:
                yield lines
                lines = []

    def get_image_url(self):
        """
        This is a function of getting image URLs.

        Returns:
            Return a URL generator.

        Raises:
            IOError: File IO error.
        """
        try:
            image_url_file = open(self.input_file_path, "r")
            url_generator = self.read_file(image_url_file)
            return url_generator
        except IOError as error:
            print(error)
            return None

