from pim.mutual_information import *


from pim.mutual_information.club import CLUB, CLUBSample
from pim.mutual_information.infonce import InfoNCE

from pim.mutual_information.l1out import L1OutUB
from pim.mutual_information.mi_knife import MIKnife
from pim.mutual_information.mine import MINE
from pim.mutual_information.nwj import NWJ
from pim.mutual_information.tuba import TUBA
from pim.mutual_information.varub import VarUB

from pim.divergence.ab_div import ABDivergence
from pim.divergence.alpha_div import AlphaDivergence
from pim.divergence.renyi_div import RenyiDivergence
from pim.divergence.beta_div import BetaDivergence
from pim.divergence.kl_div import KullbackLeiblerDivergence
from pim.divergence.lp import LP
from pim.divergence.fisher_rao import FisherRao
from pim.misc.symetrization import *


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

DISCRETE_ESTIMATORS = {
    'ab_div': ABDivergence,
    'alpha_div': AlphaDivergence,
    'renyi_div': RenyiDivergence,
    'beta_div': BetaDivergence,
    'kl_div': KullbackLeiblerDivergence,
    'lp': LP,
    'fisher_rao': FisherRao,
    'js_sym': JensenSymetrizationEstimator,
    'jf_sym': JeffreySymetrizationEstimator,

}
