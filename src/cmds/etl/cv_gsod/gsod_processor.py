import logging
from csv import DictReader as csv_dict_reader


from .gsod_data import (
    GsodData,
)

class GsodProcesser:
    
    def __init__(self, directoryList, fileProcessor):
        self.logger = logging.getLogger()
        self.directoryList = directoryList
        self.fileProcessor = fileProcessor
        self.file_count = 0
        
    def _read_file(self, file_pathname):
        self.logger.info("reading file %s ...", file_pathname)
        
        self.logger.info("done reading file...")
    
    def _process_file(self, file_pathname):        
        self.fileProcessor.process_GSOD_file(file_pathname)
    
    def process(self):
        self.logger.info("processing gsod data from url: %s, store locally in: %s", 
                         self.directoryList.get_url(), 
                         self.directoryList.get_pathname() )
        self.logger.info("gsod data files will be stored here: %s", 
                         self.fileProcessor.get_output_directory())
        
        with open(self.directoryList.get_pathname() ) as fp:
            # each line is a file url, that is opened and processed
            lines = len(fp.readlines())
            self.logger.info("processing %d gsod data files", lines)
            # need to rewind the file pointer to the beginning
            fp.seek(0)
            for line in fp:
                self.file_count += 1
                self.logger.info("Reading %d of %d: Line-%d: %s", self.file_count, lines, self.file_count, line.strip())
                self._process_file(line.strip())
                
        
        
