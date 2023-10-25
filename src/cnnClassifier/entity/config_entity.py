from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:  #(BELOW ARE THE RETURN TYPES OF THE FUNCTION)
    root_dir         : Path
    source_URL       : str
    local_data_file  : Path
    unzip_dir        : Path