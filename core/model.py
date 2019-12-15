'''
Copyright 2019-Present The OpenUEBA Platform Authors
This file is part of the OpenUEBA Platform library.
The OpenUEBA Platform is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
The OpenUEBA Platform is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with the OpenUEBA Platform. If not, see <http://www.gnu.org/licenses/>.
'''

'''
@name
@description for model sessions
'''

import logging
import threading
import time

'''
to alter deployed models set
'''
class ModelDeployment():
    def __init__(self):
        logging.info("Model Deployment made")


'''
@Session
start model session
a model session can have several jobs
'''

class Session():
    def __init__(self):
        self.selected_model_name = "SK"

    '''
    start a model session
    '''
    def start_job(name):
        logging.info("Model Server %s: starting job")
        time.sleep(2)
        logging.info("Model Server %s: finishing job")
