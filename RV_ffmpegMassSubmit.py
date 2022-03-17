''' run this script from the  batch script we use for instapy to launch in an environment
    doesnt acutally even need an environment though since it just uses the batch command


'''
import os



INPUT_DIR = 'X:\\2022_02_RV_NFT\\04_renders\\TEMP\\'
OUTPUT_DIR = 'X:\\2022_02_RV_NFT\\04_renders\\TEMPVID\\'

AUDIO_FILE = 'audiofilepath'

SCRIPT_PATH = "X:\\PIPELINE\\PYTHON\\RV_ffmpegMassSubmit\\"
DEADLINE_PATH = "C:/Progra~1/Thinkbox/Deadline10/bin/deadlinecommand.exe"

'''
seconds of hold time at end of video
'''

HOLD = '2'


def list_paths(path):
    directories = [x[1] for x in os.walk(path)]
    non_empty_dirs = [x for x in directories if x] # filter out empty lists
    return [item for subitem in non_empty_dirs for item in subitem] # flatten the list
# does not currently support sub directories
obj = os.listdir(INPUT_DIR)

# List all files and directories in the specified path
for entry in obj:

    ''' we have some built in naming conventions to consider here '''
    print(entry)

    SEQUENCE_NAME = entry
    JOB_NAME = 'RVFF_' + SEQUENCE_NAME

    JobInfo = {
        'Name': JOB_NAME,
        'Plugin': 'FFMPEG',
        'OutputDirectory0': OUTPUT_DIR,
        'OutputFilename0': SEQUENCE_NAME + ".mp4",
        }

    PluginInfo = {
        'InputFile0': INPUT_DIR + SEQUENCE_NAME + "\\" + SEQUENCE_NAME + ".0001.jpg",
        'OutputFile': OUTPUT_DIR + SEQUENCE_NAME + ".mp4",
        'OutputArgs': "-vf tpad=stop_mode=clone:stop_duration=" + HOLD + " -vcodec libx264 -crf 20 -pix_fmt yuv420p",
        'InputArgs0': "-r 30",
        'UseSameInputArgs': "False"

        }

    JOB_INFO_PATH = SCRIPT_PATH + "job_info_temp.txt"
    PLUGIN_INFO_PATH = SCRIPT_PATH + "plugin_info_temp.txt"

    with open(JOB_INFO_PATH, 'w') as f:
        for key, value in JobInfo.items():
            f.write('%s=%s\n' % (key, value))

    with open(PLUGIN_INFO_PATH, 'w') as f:
        for key, value in PluginInfo.items():
            f.write('%s=%s\n' % (key, value))


    command = DEADLINE_PATH + ' ' + JOB_INFO_PATH + ' ' + PLUGIN_INFO_PATH
    #print(command)
    os.system(command)
