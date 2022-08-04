import sys
import os
print(os.getcwd())
sys.path.append(os.path.join(os.getcwd(),'divergence/'))
sys.path.append(os.path.join(os.getcwd(),'continuous_gaussian/'))
sys.path.append(os.path.join(os.getcwd(),'entropy/'))
sys.path.append(os.path.join(os.getcwd(),'mutual_information/'))
sys.path.append(os.path.join(os.getcwd(),'misc/'))

from continuous_gaussian import *
from divergence import *
from entropy import *
from mutual_information import *
from misc import *
