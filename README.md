# Ranking object detection papers by citation
Last updated: 18 june 2019

List of algorithms (papers with open source code) researched for object detection (bounding box, semantic segmentation, instance segmentation). This repository is mainly used as a citation reference for my master's dissertation. 

There are three TXT files:
* [Bounding box file](articles_object_detect.txt)
* [Semantic segmentation file](articles_semantic_segmentation.txt)
* [Instance segmentation file](articles_instance_segmentation.txt)

Each contains data organized in a CSV style, where:
* The first row has only informative data
* The first column has the year the paper was published
* The second column has the number of cites it had at the time I searched for the paper
* The third column has the main name of the algorithm

There is also a Python script that generates the charts shown in my master's document which highlights the top **X%** most cited papers, in such a way that visualization of the most relevant works is easy to see. **X** is by default 10, but the user can change it via flag commands.
## Getting started
### Prerequisites
*The following steps are only necessary if you want to run the python script that orders the lists and generates the charts :)
* Python3
### Installation

1. Clone this repository
```
git clone https://github.com/AlanNaoto/papers_and_code_ranking
```
2. Install dependencies
```
pip3 install -r requirements.txt
```
Done, simple as that!
### Running the script
Navigate to the downloaded directory.
```
cd ~/papers_and_code_ranking
```
And run the script. The generated charts are saved on the same dir as the main.py file
```
python3 main.py --Update with flag commands here! (X%)
```
