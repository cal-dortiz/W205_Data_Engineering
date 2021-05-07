# Project 2: Tracking User Activity
## W205
## Dan Ortiz
## 10/25/2020

### Summary

The goal of this project is to show what kind of data customers will have access to and what kind of business questions they can answer from the data collected on our tech-ed service. A Few insights are:

   * 390 Students have taken "Learning Git" and it is by far the most popular course
   * The least popular courses with 1 complete assessment each are:
       * Nulls, Three-valued Logic and Missing Information
       * Native Web Apps for Android
       * Learning to Visualize Data with D3.js
       * Operating Red Hat Enterprise Linux Servers
   * Currently, there are no students taking any courses for certification

### How This Project is Structured

There are two main files for this project. They are:
   - pipeline_startup.sh
   - Dan_Ortiz_Assignment_2_report.ipynb
   
The pipeline_startup.sh file contains the script to spin up the docker cluster, the Kafka code, and the code to launch
the Jupyter Notebook. Once inside the notebook, you will see the Spark/PySpark code, the schema design, and 

### How to Load

   1. Download all files to a single directory
   2. Run ```sh pipeline_startup.sh``` to run the shell script
   3. Copy and paste the Jupyter Notebook url posted to the CLI
   4. If you are running this from a cloud VM replace the local (0.0.0.0) with the IP of the cloud instance
   5. This will bring up Jupyter Notebooks, simply navigate to the file named "Dan_Ortiz_Assignment_2_report"
   6. When your session is finished return to the CLI and hit ```CTRL + C``` to close the Jupyter kernel
   7. Type ```docker-compose down``` to shut down the docker cluster and return to the native CLI

### Technologies Used
   - Linux Command Line (Ubuntu used)
   - Docker
   - Docker-compose - Used to manage the docker cluster (must install the docker-compose app. See Technologies Required)
   - jq: Used to break apart the json file into individual submissions
   - Kafka: Used to generate messages\events into topic from the parsed json file
   - Spark: Takes the messages\events from Kafka to construct a schema and dataframe.
   - Jupyter Notebook: Hosts the analytics of the data set
   - Pandas: Used to convert data from SparkSql queries to a prettier output.
   - Zookeeper: Used as the data broker between Kafka and spark
   - MIDS: General purpose environment for UC Berkeley MIDS program
   
### Technologies Required

In order to run this analysis you need to be running Linux (preferably Ubuntu Linux) and have docker downloaded and working.

   - Ubuntu: [Link to Ubuntu](https://ubuntu.com/)
   - Docker : [Link to Docker](https://www.docker.com/)
   - Docker-Compose:
      - On Linux, in the CLI run the following command: sudo apt-get docker-compose

### Technologies used in docker-compose file

The following packages will be downloaded and configured into their own containers during the first initialization of the pipeline_startup.sh shell. Therefore having Linux and docker installed on the machine is sufficient:

   - jq
   - Kafka
   - Spark
   - Jupyter Notebook
   - Zookeeper
   - MIDS

### File Locations and Git Structure

There are two main files that you will need to interface with. The rest of the files support.

The link to the main files are below:

   - [Final Report](Dan_Ortiz_Assigment_2_report.ipynb) - connects to the Kafka topic, builds the dataframe schema, analysis of the data 
   - [pipeline_startup](pipeline_startup.sh) - Calls docker-compose, gets the data and processes it into a Kafka topic
   
   
 The supporting files are the following:  
   - [docker_compose](docker-compose.yml) - Spins up docker cluster and bridges. It is called in the pipeline startup.
   - [session history](dortiz_history.txt) - CLI Session history
   - [local data save](assessment-attempts-20180128-121051-nested) - local copy of the data. It will be refreshed during the pipeline startup
   
## Note to TA's.

I realized I failed to initiate a branch at the beginning of my project and thus committed to master. I caught the mistake and move all these files into a branch repo and reset the master to commit 12d6eb4 using git reset.
