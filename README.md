# COS-526-Neural-Rendering-Project
To get the inference results, we must run BundleTrack, instant-ngp and Xmem.

To run the project, first download the datasets -  [NOCS Dataset](https://github.com/hughw19/NOCS_CVPR2019) and place in ./NOCS, 
[YCBInEOAT Dataset](https://archive.cs.rutgers.edu/archive/a/2020/pracsys/Bowen/iros2020/YCBInEOAT/) and place in ./YCBInEOAT or your use your own dataset.

To get the segmentation masks, we run XMeM, instructions can be found in this [tutotrial](https://colab.research.google.com/drive/1RXK5QsUo2-CnOiy5AOSjoZggPVHOPh1m?usp=sharing)

To run:

- `cd [to project path]`
- `rm -rf build`
- `mkdir build`
- `cd build && cmake .. && make`

If this does not work, please follow instructions use this docker [image](https://github.com/wenbowen123/BundleTrack/issues/63)  (tested on 4090Ti)

Once this is run:

Change `model_name` and `model_dir` in `config_[modelname].yml` to the path to the .obj file

- Open a separate terminal and run
  - `bash lf-net-release/docker/run_container.sh`
  - `cd [path_to_proj]`
  - `cd lf-net-release && python run_server.py`
 

- Go back to the terminal where you launched the project (or bunldeTrack Docker) and run below. The output will be saved based on output dir mentioned inthe yml file

  `python scripts/run_[model_name].py --data_dir [path to proj] --port 5555 --model_name [.obj file you are running for]`
  
Once you get the pose outputs, we must run:
 - First edit the dir locations at the bottom of scripts/getMaskedImages to run to get masked object images
 - Then edit the dir location at the botton of scripts/Convert_Txt_to_Json to get the json needed for instant-ngp

Run instant-ngp using the output of masked images and the converted json file using `./instant-ngp [path to data file]`


