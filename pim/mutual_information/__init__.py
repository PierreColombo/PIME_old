import sys

sys.path.append('mutual_information/')
sys.path.append('../misc/')
sys.path.append('../entropy/')
from utils import *
from club import CLUB, CLUBSample
from gaussian_fisher_rao import FisherRao
from gaussian_frechet import Frechet
from gaussian_js import JensenShannon
from infonce import InfoNCE

from l1out import L1OutUB
from mi_knife import MIKnife
from mine import MINE
from nwj import NWJ
from tuba import TUBA
from varub import VarUB


MI_CONTINUOUS_ESTIMATORS = {
    'club': CLUB,
    'club_sample': CLUBSample,
    'infonce': InfoNCE,
    'l1out': L1OutUB,
    'mi_knife': MIKnife,
    'mine': MINE,
    'nwj': NWJ,
    'tuba': TUBA,
    'varub': VarUB,

}
