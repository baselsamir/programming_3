# Complex subsystem classes
class DatabaseManager:
    def connect(self):
        print("Connected to database.")

    def disconnect(self):
        print("Disconnected from database.")

class FileSystemHandler:
    def open_file(self, filename):
        print(f"Opened file: {filename}")

    def close_file(self, filename):
        print(f"Closed file: {filename}")

class CompressionUtility:
    def compress(self, file):
        print(f"Compressed file: {file}")

    def decompress(self, file):
        print(f"Decompressed file: {file}")

class ImageProcessingModule:
    def process_image(self, image):
        print(f"Processed image: {image}")


# Facade class
class MultimediaFacade:
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.file_system_handler = FileSystemHandler()
        self.compression_utility = CompressionUtility()
        self.image_processing_module = ImageProcessingModule()

    # High-level methods provided by the facade
    def import_image(self, filename):
        self.database_manager.connect()
        self.file_system_handler.open_file(filename)
        self.compression_utility.decompress(filename)
        self.image_processing_module.process_image(filename)
        self.file_system_handler.close_file(filename)
        self.database_manager.disconnect()


# Client code
facade = MultimediaFacade()
facade.import_image("example.jpg")