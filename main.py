
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
shot = ['T', 'L', 'R'];
selfurl = 'https://cloud-run-hackathon-python-2qprbru23q-uc.a.run.app'

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    curstate= requset.state
    curX = curstate[2]
    curY = curstate[3]
    curDirect = curstate[4]
    curwashit = curstate[5]
    curscore = curstate[6]
    
    app.logger.info (curX)
    
    #selfurl = request.values.get('self')
    # return moves[random.randrange(len(moves))]
    return moves[random.randrange(len(moves))]
 

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
