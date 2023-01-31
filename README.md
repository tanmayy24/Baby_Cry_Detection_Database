# Baby_Cry_Detection_Database

## Description
This dataset is a subset of the AudioSet, curated for Baby-cry detection task.<br />
**The curated dataset is divided into**:
1. **development set**:<br />
   The development dataset is further split into the _TRAIN_ and _VALIDATION_ sets.
3. **evaluation set**

The dataset has been categorized into two main classes: `BabyCry` and `Other`. <br />
The `Other` class comprises of sound clips from the domestic household environment. <br />
**Note**: <br />
    The recurrence of the events in the labels for each clip does not overlap. <br />
    The dataset contains an almost equal distribution of clips between `BabyCry` and `Other` classes. <br />

The distribution for the dataset is as follows: <br />
<table>
<thead>
<tr>
<th style="text-align:center"><strong>SET</strong></th>
<th style colspan="2"="text-align:center"><strong>development set</strong></th>
<th style="text-align:center"><strong>evaluation set</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><strong>CLASS</strong></td>
<td style="text-align:center" ><em>TRAIN</em></td>
<td style="text-align:center"><em>VALIDATION</em></td>
<td style="text-align:center"><em>TEST</em></td>
</tr>
<tr>
<td style="text-align:center"><strong>BabyCry</strong></td>
<td style="text-align:center">492</td>
<td style="text-align:center">39</td>
<td style="text-align:center">25</td>
</tr>
<tr>
<td style="text-align:center"><strong>Other</strong></td>
<td style="text-align:center">480</td>
<td style="text-align:center">39</td>
<td style="text-align:center">40</td>
</tr>
<tr>
<td style="text-align:center"><strong>TOTAL</strong></td>
<td style="text-align:center">972</td>
<td style="text-align:center">78</td>
<td style="text-align:center">65</td>
</tr>
</tbody>
</table>

## TSV file format
The strong annotations are provided in a tab separated csv file under the following format: <br />
`[filename (string)][tab][event_label (string)][tab][onset (in seconds) (float)][tab][offset (in seconds) (float)][tab][start (in seconds) (float)][tab][name (string)][tab][original_label (string)]`<br />

filename: name of the audio file from where the 10-second clip was extracted t=start sec to t=start+10 sec, correspond to the clip boundaries within the full video. <br />
event_label: updated class of the sound event as per our dataset distribution.<br />
onset: onset time in seconds.<br />
offset: offset time in seconds.<br />
start: start of where the 10-second clip was extracted as t=start sec to t=start+10 sec.<br />
name: name of the audio file.<br />
original_label: original class of the sound event as present in AudioSet.<br />

## Dataset Download
`requirements.txt` is available to download the dependencies required to download the dataset.

After downloading the dependencies, you can download the dataset using the script: 
`download_audioset_baby_cry_dataset.py`. <br />It requires two arguements: `workspace` and `data_type`.<br />
### Usage:
Here are the commands to download train, validation, and test dataset respectively:<br />
`python download_audioset_baby_cry_dataset.py --workspace=$WORKSPACE --data_type=train`<br />
`python download_audioset_baby_cry_dataset.py --workspace=$WORKSPACE --data_type=validation`<br />
`python download_audioset_baby_cry_dataset.py --workspace=$WORKSPACE --data_type=test`<br />
(You can change workspace to the desired working folder.) <br />
This will store the dowloaded files in the dataset folder created in the `workspace` under train, validation, and test respectively. 

## Summary
This codebase provides the dataset useful for baby cry studies in the domestic environment.

## Citation
**If this database is helpful, please feel free to cite the following paper:**

Tanmay Khandelwal, Rohan Kumar Das, and Chng Eng Siong, “Is Your Baby Fine at Home? Baby Cry Sound Detection in Domestic Environments”, in Asia-Pacific Signal and Information Processing Association (APSIPA) Annual Summit and Conference (ASC), Chiang Mai, Thailand, pp. 275–280, 2022. <br />
To access the paper<br />
[IEEEXplore](https://ieeexplore.ieee.org/document/9980350) || [APSIPA ASC](http://www.apsipa.org/proceedings/2022/APSIPA%202022/TuPM1-1/1570830955.pdf) ||

**BibTex reference <br />**
@INPROCEEDINGS{9980350,
  author={Khandelwal, Tanmay and Das, Rohan Kumar and Chng, Eng Siong},
  booktitle={2022 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC)}, 
  title={Is Your Baby Fine at Home? Baby Cry Sound Detection in Domestic Environments}, 
  year={2022},
  volume={},
  number={},
  pages={275-280},
  doi={10.23919/APSIPAASC55919.2022.9980350}}



