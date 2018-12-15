## Simple video converter commandline tool

#### Inspiration
A friend of mine in the office needed mp3 file formats of some songs (six precisely) that were in video format, I quickly opened vlc video player and started converting, the process took about 73 minuites, i got tired of waiting, i saw some tools like video converter that required me to download the software, there are some online applications for the same but din't impress me, that what led to creation of this simple commandline tool.

#### Description
It's so simple to follow along, <br/>
1. Place your files in one folder that needs conversion, then that becomes the data path.
2. Provide a destination path where your files will be stored.
3. Specify number of threads to perform conversion, e.g if you have 10 files you might need 10 threads for quick conversion, default number is 20
4. Finally specify the output conversion format eg. mp3 Nb(only mp3 is currently supported in version 1)

#### Example
###### python converter.py -dp C:\Users\DMMURIITHI\Desktop\projects\AudioConverter\data -dd C:\Users\DMMURIITHI\Desktop\ -f mp3

#### Installations
1. ensure python 3.6 and above is installed
2. Run pip install -r requirements.py to install the requirements


#### simple video converter commandline tool

 optional arguments: <br/>
  -h, --help            show this help message and exit  <br/>
  -v, --version         Displays version and exits.  <br/>
  -t, --threads         Number of Concurrent conversions.  <br/>
  -dp DATAPATH, --datapath DATAPATH
                  The path to the data converted  <br/>
  -dd DESTINATIONDIRECTORY, --destinationdirectory DESTINATIONDIRECTORY
                    destination directory path, a new foder 'converted'  will be created  <br/>
  -f {mp3,mp4,webm}, --format {mp3,mp4,webm}
                     The desired output file format  <br/>

#### Author
Muriithi Derrick
