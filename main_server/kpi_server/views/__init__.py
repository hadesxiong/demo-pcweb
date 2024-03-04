# conding=utf8

# user接口
from .user.getUserList import *
from .user.updateUser import *
from .user.createUser import *

# org接口
from .org.getOrgList import *
from .org.updateOrg import *
from .org.getOrgInfo import *

# other接口
from .other.getFilter import *
from .other.generateDetail import *

# rank接口
from .rank.getRank import *
from .rank.getRankV2 import *
from .rank.getSingleRank import *

# table接口
from .table.getTableData import *
from .table.getTableFilter import *

# auth接口
from .auth.userLogin import *
from .auth.refreshToken import *

# dashboard接口
from .dashboard.getDashboard import *

# upload接口
from .upload.getUploadList import *
from .upload.getUploadDetail import *
from .upload.updateUpload import *

# score接口
from .score.getScoreTable import *
from .score.getScoreData import *
from .score.getScoreRule import *

# factor接口
from .factor.getFactorList import *
from .factor.updateFactor import *
