import argparse
import sys
import os
import glob
import logging
import moviepy.editor as mp
import threading
from queue import Queue

VERSION = 'Version 1'
queue = Queue()
_FORMATS = ('mp3','mp4','webm')

DEST_PATH =''
FILES = []

def set_destination(destpath):
    ''' 
    Create a folder called converted to store the converted files

    '''
    if not os.path.exists("converted"):
        print("creating....")
        try:
            os.makedirs(destpath+"/converted")    
        except FileExistsError:
            print("That folder exists.")
    DEST_PATH = destpath+"/converted"
    
    print("setting destination folder")
    print("Destination path is %r "%DEST_PATH)
    return DEST_PATH


def begin_convertion(f):
    '''
    Each Thread uses this function to convert a file
    '''
    ct = threading.currentThread()
    head, tail = os.path.split(f)
    name,ext = tail.split(".")
    print("Reading... %s" %name)
    try:
        clip = mp.VideoFileClip(f)
        print("Converting ... %s" %name)
        rawstring = ct._args[0]+"/"+name+".mp3"
        formatedstr = rawstring.replace('\\','/')
        
        # clip.audio.write_audiofile(formatedstr)
    except Exception as e:
        print("Error writting file")
        print(e)
        sys.exit(0)


# Create worker threads (will die when main exits)
def create_workers(threads,df):
    print("Creating %r workers"%threads)
    for _ in range(threads):
        t = threading.Thread(target=work,args=(df,))
        t.daemon = True
        t.start()

# Do the next job in the queue
def work(x):
    print("Issuing jobs")
    while True:
        task = queue.get()
        begin_convertion(task)
        queue.task_done()

# Each file in a folder is s a new job
def create_jobs(files):
    for f in files:
        queue.put(f)
    queue.join()


def check_folder_exists(args):
    '''This methods checks if the provided data folder exists '''

    status = []
    for path in args:
        try:
            if os.path.exists(path) is False:
                status.append("Directory %r does not exist"%path)
            else:
                status.append(True)

        except Exception as e:
            status.append("Please check on slashes.")
            continue
    return status


def main():
   
    """ 
    Program entry point
    Start by fetching data from the Commandline

    """
    parser = argparse.ArgumentParser(description="simple video converter commandline tool")
    parser.add_argument('-v','--version', action='store_true', default=False,help='Displays version and exits.')
    parser.add_argument('-t','--threads', action='store_true', help='Number of Concurrent conversions.')
    parser.add_argument('-dp', '--datapath', help="The path to the data converted",type=str)
    parser.add_argument('-dd', '--destinationdirectory', help="destination directory path, a new foder 'converted' will be created ",type=str)
    parser.add_argument('-f', '--format', help="The desired output file format",choices=_FORMATS,type=str)

    args = parser.parse_args()
    print(args)
    
    if args.version:
        print(VERSION)
        sys.exit(0)

    if args.threads is False:
        args.threads = 20
    
    if args.datapath is None and args.destinationdirectory is None and args.format is None:
        parser.print_usage()
        sys.exit(0)

    if args.datapath is None:
        print("You need to provide a data directory path")
        parser.print_usage()
        sys.exit(0)
    
    if args.destinationdirectory is None:
        print("You need to provide a data destination directory path")
        parser.print_usage()
        sys.exit(0)
    
    if  args.format is None and args.format not in _FORMATS:
        print("You cannot privide %r format" %args.format)
        parser.print_usage()
        sys.exit(0)

    # cleaned data
    datapath = args.datapath
    destinationpath = args.destinationdirectory
    format = args.format
    NUMBER_OF_THREADS = args.threads

    # check whether the provided paths are valid paths
    paths = [datapath,destinationpath]
    status = check_folder_exists(paths)
  
    if status[0] is not True or status[1] is not True:
        print(status)
        sys.exit(0)
    else:
        # The folders are ok
        print("ok")

        # check if the data folder has data
        arr = os.listdir(datapath)
        # Fetch files with absolute path
        absfilepath = [datapath+'/'+i for i in arr]
    
        print("These are the files to be converted into %r format \n"%format)
        x=1
        for i in arr:
            print(str(x)+"."+i)
        print("\n")
        
        _OPTIONS=('1','2',"yes","no")
        SELECTING = True

        try:
            while SELECTING:
                option = input("Sure to proceed? \n 1.Yes \n 2. No \n")

                if option not in _OPTIONS:
                    print("Please select 1 or 2 or Yes or No \n")
                    
                else:
                    SELECTING=False
                    if option is '1' or option is 'yes':
                        print("Almost there .... \n")
                        df = set_destination(destinationpath)
                        create_workers(NUMBER_OF_THREADS,df)
                        create_jobs(absfilepath)

                    elif option is '2' or option is 'no':
                        print("Thanks for using this tool")
                        sys.exit(0)
                    
        except KeyboardInterrupt:
            print("Thanks for using this tool")

if __name__ == '__main__':
    main()