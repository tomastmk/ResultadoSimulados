class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'

def print_progress(i, total) -> None:
    
    progress = i / total * 100
    print(bcolors.BOLD+f"Progress: {progress:.1f}%"+bcolors.ENDC, end="\r")
