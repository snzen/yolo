from models import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cfg', type=str, help='Darknet cfg')
parser.add_argument('--weights', type=str, help='')
opt = parser.parse_args()


convert(opt.cfg, opt.weights)
