# Cluster and Cloud Computing (COMP90024) 2022 Sem 1 - Team 34
Team members:
- Juny Kesumadewi (197751)
- Georgia Lewis (982172)
- Vilberto Noerjanto (553926)
- Matilda O’Connell (910394)
- Rizky Totong (1139981)

## Website URL
http://172.26.130.122/

## YouTube URL
Website: https://www.youtube.com/watch?v=vs5yVu1PYjY

Ansible playbook: https://www.youtube.com/watch?v=qJfhd95PH_U

## Repository Notes

This repository consists of several components:

* `website`: Flask web application backend and React frontend.
* `harverster`: Python application to harvest Tweets.
* `analysis`: Various Python scripts used to load external data such as AURIN census data and historic Twitter data. 
* `annotator`: Pytahon application to append extra information into Tweets saved in CouchDB database. Specifically it was used to annotate Local Government Area (LGA) to a Tweet based on its geo location.
* `infrastuctures`: Ansible scripts to spin up the infrastructures to host these applications.
* `map_reduce`: Javascripts used to create CouchDB MapReduce views.

Each directory has more detailed READMEs on how to set up each independent component.
