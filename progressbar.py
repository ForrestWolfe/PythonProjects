import time
import random


def getprogressbar(progress, total, barWidth=20, duration=1.0):
    """Returns a string that represents a progress bar that has 'barwidth'
    bars and has progressed 'progress' amount out of a total amount"""
    progressBar = ''
    progressBar += '['  # printing left side of progress bar
    # make sure the amount of progress is between zero and total
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of bars to display
    numberOfBars = int((progress / total) * barWidth)
    progressBar += "*" * numberOfBars
    progressBar += ' ' * (barWidth - numberOfBars)
    progressBar += ']'  # the end of the progressbar

    # calculating the percentage that is complete
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar


# Simulating the progress bar
print('press CTRL-Z to quit')
bytesDownloaded = 0
downloadSize = 4098
while bytesDownloaded < downloadSize:
    # 'simulating a download of bytes
    bytesDownloaded += random.randint(0, 100)

    # get the progress bar string fo rthis amount of progress
    barStr = getprogressbar(bytesDownloaded, downloadSize)

    # don't print a newline at the end, and immediately flush the
    # printed string to the screen
    print(barStr, end='', flush=True)
    # pause
    time.sleep(1)
    # prints backspaces to erase the previously printed progress bar:
    print('\b' * len(barStr), end='', flush=True)
