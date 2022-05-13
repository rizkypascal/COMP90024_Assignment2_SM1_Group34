# MRC Infrastructures

The virtual machines are hosted on Melbourne Research Cloud infrastructures.

This folder contains the ansible scripts used to set up the existing infrastructures that consist of:
* Three virtual machines (VMs) named:
  * master
  * worker-1
  * worker-2
* Three volumes
  * master-vol-1: attached to master
  * worker-1-vol-1: attached to worker-1
  * worker-2-vol-1: attached to worker-2

## Applications currently running
* Three nodes of CouchDB databases belong to the same cluster: there is one node of CouchDB database running on each of the VMs. They were running on Docker containers and were set up manually.
* One harvester running on each of the VMs. They are running on Docker container and were deployed manually using Docker Compose.
* One annotator whose job is to look for Tweet that does not annotation and annotate it. In this project, we specifically want to annotate Local Goverment Area of the geo location of a Tweet.
* A web application running on `master` vm. It is running on Docker containers and were deployed manually using Docker Compose.

## Dynamic application deployment
By running this ansible script again, 
in addition to the existing infrastructure, you will get the following:
* A new VM
* A harvester running in this VM: connected to the existing CouchDB node as specified in `host_vars/harvester.yaml`.
* An annotator running in this VM: connected to the existing CouchDB node as specified in `host_vars/harvester.yaml`.

## Usage

To run this ansible script, you will need to download your openrc.sh file containing your credentials on MRC.

Then name it `openrc.sh` in this folder and execute:
```
bash run-nectar.sh
```