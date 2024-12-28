#!/usr/bin/env python

##################### Simple Manual to Use This Script #####################
# - Add this directory outside your project
# - Run these following commands:
#       [You could run this once after adding these directories]
#       chmod +x ../rails-solargraph-config/add_rails_solargraph_config.py
#       [Run this command to add the solargraph config files to your Rails
#        projects]
#       ../rails-solargraph-config/add_rails_solargraph_config.py
#
# - Enjoy Rails Solargraph!
############################################################################

# import the needed general Python modules
import os
import shutil

# Solargraph configurations for Rails to be copied
project_path = os.getcwd()
solargraph_path = os.path.join(project_path, r"../rails-solargraph-config/")
files = [r".solargraph.yml", r".solargraph_definitions.rb"]

# Copy the files to the Rails project
for file in files:
    shutil.copy(os.path.join(solargraph_path, file), project_path)