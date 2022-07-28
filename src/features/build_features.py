# make_dataset.py
#!/usr/bin/env python
# coding: utf-8
# Import libraries

import logging
import pandas as pd
import numpy as np
import argparse
import text_feature_engineer as text_feateng
#from feateng_tabular import build_numerical_feateng, build_cat_le, build_cat_from_le



def main(input_file, output_file):
    """ 
        You must define here how to build any features engineer from data
        :data: dataset from where features will be made
        :features: final dataset with all features eng
    """

    logger = logging.getLogger(__name__)
    logger.info('INIT: build features engineer from processed data')

    logger.info('RUN: loading data')
    #df = load_data(input_file, kind='csv')
    data_df = pd.read_csv(input_file)
   
   
    logger.info(f'RUN: data size before be processed: {data_df.shape}')
    
    logger.info(f'RUN: building features')

   
    # ****************************************************** # 
    # put here what you think is needed to build features 
    # ****************************************************** #
    
    pastpayment_vars = ['pay_0', 'pay_2', 
                        'pay_3', 'pay_4', 
                        'pay_5', 'pay_6']
    data_df["pastpayment_acum"] = data_df[pastpayment_vars].sum(axis=1)

    bill_amount_vars = ['bill_amt1', 'bill_amt2',
                        'bill_amt3', 'bill_amt4', 
                        'bill_amt5', 'bill_amt6']

    data_df["bill_amount_acum"] = data_df[bill_amount_vars].sum(axis=1)

    bill_amount_vars.reverse()
    bill_amount_tend_df = data_df[bill_amount_vars].pct_change(axis="columns").replace(np.inf, 0).replace(np.nan, 0)

    bill_amount_tend_df.rename(columns={"default payment next month": "target"}, inplace=True)

    bill_amount_tend_df.columns = ['tend_bill_amt6', 'tend_bill_amt5', 'tend_bill_amt4', 'tend_bill_amt3', 'tend_bill_amt2',
        'tend_bill_amt1']

    bill_amount_tend_df.drop("tend_bill_amt6", axis=1, inplace=True)

    data_df = data_df.join(bill_amount_tend_df)


    pay_amount_vars = ['pay_amt1', 'pay_amt2', 
                        'pay_amt3', 'pay_amt4', 
                        'pay_amt5', 'pay_amt6']

    data_df[pay_amount_vars]

    data_df["payment_amount_acum"] = data_df[pay_amount_vars].sum(axis=1)



    pay_amount_vars.reverse()
    pay_amount_tend_df = data_df[pay_amount_vars].pct_change(axis="columns").replace(-np.inf, 0).replace(np.inf, 0).replace(np.nan, 0)

    pay_amount_tend_df.rename(columns={"default payment next month": "target"}, inplace=True)

    pay_amount_tend_df.columns = ['tend_pay_amt6', 'tend_pay_amt5', 'tend_pay_amt4', 'tend_pay_amt3', 'tend_pay_amt2',
        'tend_pay_amt1']

    pay_amount_tend_df.drop("tend_pay_amt6", axis=1, inplace=True)

    data_df = data_df.join(pay_amount_tend_df)

    predictors = [
        'limit_bal', 'sex', 'education', 'marriage', 'age',
        'pay_0','pay_2','pay_3','pay_4','pay_5','pay_6', 'bill_amt2',
        'bill_amt4', 'bill_amt6', 'pay_amt1', 'pay_amt2',
        'pay_amt3', 'pay_amt4', 'pay_amt5', 'pay_amt6', 
        'pastpayment_acum', 'bill_amount_acum', 'tend_bill_amt5',
        'tend_bill_amt4', 'tend_bill_amt3', 'tend_bill_amt2', 'tend_bill_amt1',
        'payment_amount_acum', 'tend_pay_amt5', 'tend_pay_amt4',
        'tend_pay_amt3', 'tend_pay_amt2', 'tend_pay_amt1'
    ]

    data_df = data_df[predictors + ['kfold','target']]
    data_df.replace([np.inf, -np.inf], 0, inplace=True)
    data_df.replace([np.nan], -9999, inplace=True)
    logger.info(f'RUN: data size after be processed: {data_df.shape}')


    logger.info(f'RUN: saving features')
    #save_data(output_file, features)
    data_df.to_csv(output_file, index=False)

    logger.info('END: making features data set has finished.')

if __name__ == "__main__":
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    #project_dir = Path(__file__).resolve().parents[2]
    
    parser = argparse.ArgumentParser()
    parser.add_argument( "--input_file",   required=True, 
        help="Specify file name without extension from processed folder from where features will be built.", type=str)
    parser.add_argument( "--output_file",   required=True, 
        help="Specify output file name which will be saved into features folder.", type=str)

    args = vars(parser.parse_args())
    
    main(input_file=args['input_file'], output_file=args['output_file'])