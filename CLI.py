import argparse
from model.ptediction import prediction


parser = argparse.ArgumentParser(description='Predict the Outcomes on model and values')
parser.add_argument('--prediction_model',action='store',  dest='prediction_model', type=str, nargs=1, help='model on which the Outcome will predicts')
parser.add_argument('--prediction_params', action='append',  dest='prediction_params', type=float, nargs=8, help='the values on Outcome will predicts')
args = parser.parse_args()
print(prediction(args.prediction_model[0], args.prediction_params))