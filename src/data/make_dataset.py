# make_dataset.py
#!/usr/bin/env python
# coding: utf-8
# Import libraries
import logging
import pandas as pd
from pathlib import Path
import argparse



def main(input_file, output_file):
    """ Runs data processing scripts to turn raw data from raw data into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('INIT: making final data set from raw data')

    logger.info('RUN: Loading data')
    data = pd.read_excel(input_file, header=1)
    
   
    logger.info(f'RUN: Data size before be processed: {data.shape}')
    
    logger.info(f'RUN: Processing data')

    # ****************************************************** # 
    # put here what you think is needed to build features 
    # ****************************************************** #
    



    data.rename(columns={"default payment next month": "target"}, inplace=True)
    data.rename(columns=str.lower, inplace=True)


    logger.info(f'RUN: Data size after be processed: {data.shape}')

    logger.info(f'RUN: Saving data')
    data.to_csv(output_file, index=False)

    logger.info('END: raw data processed.')

if __name__ == "__main__":
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    parser = argparse.ArgumentParser()
    parser.add_argument( "--input_file",   required=True, 
        help="Specify file name without extension from raw folder to be processed.", type=str)
    parser.add_argument( "--output_file",   required=True, 
        help="Specify output file name which will be saved into folder processed.", type=str)

    args = vars(parser.parse_args())
    
    main(input_file=args['input_file'], output_file=args['output_file'])