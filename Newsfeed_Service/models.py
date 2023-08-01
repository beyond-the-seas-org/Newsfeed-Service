#this file is just only for recognizing all model class to the running program 

import sys
 
# append the path of the
# parent directory
sys.path.append("..") #this is needed to import file from sibling directory

from Database_Service.models.tables import * 
from Database_Service.models.student import *
from Database_Service.models.project import *
from Database_Service.models.field import * 
from Database_Service.models.publication import * 
from Database_Service.models.post import * 
from Database_Service.models.comment import * 
from Database_Service.models.community import * 
