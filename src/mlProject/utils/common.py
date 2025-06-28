import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import Box
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    ''' reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        Box: Box type
            
    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfuly")
            return Box(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    '''Create a list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ingore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to False
    '''
    
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
       
     
@ensure_annotations
def save_json(path: Path, data: dict):
    '''save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    '''
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> Box:
    '''load json file data
    
    Args:
        path (Path): path to the json file
        
    Returns:
        Box: data as class attributes instead of dict
    '''
    
    with open(path) as file:
        content = json.load(file)
    
    logger.info(f"json file loaded successfuly from {path}")
    return Box(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    '''Save binary file
    
    Args:  
        data (Any): data to be saved as binary file
        path (Path): path to binary file
    '''
    
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at {path}")
   
 
@ensure_annotations
def load_bin(path: Path) -> Any:
    '''load binary file
    
    Args:
        path (Path): path to binary file
        
    Returns:
        Any: object stored in the data
    '''
    
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    

@ensure_annotations
def get_size(path: Path) -> str:
    '''get size in KB
    
    Args:
        path (Path): path to the file
        
    Returns:
        str: size in KB
    '''
    
    size_in_kb = round(os.path.getsize(path)/1024)
    
    return f"~ {size_in_kb} KB"
    
    
