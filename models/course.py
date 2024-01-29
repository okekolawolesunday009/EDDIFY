#!/usr/bin/python3
"""holds class course"""

import models
from models.base_model import BaseModel

class course(BaseModel):
	course_id = ""
	course_name = ""
	category = ""
	author_id = ""
