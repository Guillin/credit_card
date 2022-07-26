# config.py
INPUT_PATH = "data/raw/"
OUTPUT_PATH = "data/features/"
#ROOT_DIR = args.root_dir
NJOBS = -1
VERBOSE = 1
PLOT = False
SEED = 47


# Specify numerical and categorical features in order to be processed adecually
num_features = ["age", "campaign", "pdays", "previous", "emp.var.rate", 
                "cons.price.idx", "cons.conf.idx","euribor3m", "nr.employed"]

cat_features = ["job", "marital", "education","default", "housing", "loan",
                "contact", "month", "day_of_week", "poutcome"]

# Specify which would be the target feature
target = "target"

colors = {
'RED'   : "\033[1;31m" , 
'BLUE'  : "\033[1;34m",
'CYAN'  : "\033[1;36m",
'GREEN' : "\033[0;32m",
'RESET' : "\033[0;0m",
'BOLD'    : "\033[;1m",
'REVERSE' : "\033[;7m"
}