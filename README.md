# Melbourne Twitter Analysis

This repository consists of several independent projects.
They have been combined into one repository for the convenience of the subject assessment.

* `website`: Flask web application backend and React frontend.
* `harverster`: Python application to harvest Tweets.
* `analysis`: Various Python scripts used to load external data such as AURIN data and historic Twitter data. 
* `annotator`: Pytahon application to append extra information into Tweets saved in CouchDB database. Specifically it was used to annotate Local Government Area (LGA) to a Tweet based on its geo location.
* `infrastuctures`: Ansible scripts to spin up the infrastructures to host these applications.
* `map_reduce`: Javascripts used to create CouchDB MapReduce views.

Please visit each directory on details of how to set up each independent application.