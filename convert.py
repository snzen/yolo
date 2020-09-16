from models import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cfg', type=str, help='Darknet cfg')
parser.add_argument('--pt', type=str, help='.pt files')
opt = parser.parse_args()


convert(opt.cfg, opt.pt)
