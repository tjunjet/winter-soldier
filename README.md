# winter-soldier
This repository will contain the required software we are using for the winter-soldier. For now, it is mainly the computer vision model as well as the front-end application.

# Pre-requisities
1. Install Anaconda or Miniconda (You can use any virtual environment you like, but I personally prefer to use Anaconda)

# Instructions on how to use the repository
1. Clone the repository
```sh
git clone https://github.com/tjunjet/winter-soldier.git
```

2. Create a conda environment, we will be using Python 3.8.10 for this
```sh
conda create --name robotEnv python=3.8.10
conda activate robotEnv
```

3. Install the required dependencies
```sh
cd winter-soldier/yolov5
pip install -r requirements.txt
``` 

4. Run the detection model filtered for humans from shell
```sh
sh human_detection.sh
```
