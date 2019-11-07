# Animation of a DNA double helix

import random, time

rows = [
    '                $$',
    '              ${}-{}$',
    '             ${}---{}$',
    '            ${}-----{}$',
    '           ${}------{}$',
    '           ${}------{}$',
    '            ${}----{}$',          
    '             ${}--{}$',
    '               $-$',
    '              $--$$',
    '             ${}---{}$',
    '            ${}----{}$',
    '           ${}------{}$',
    '           ${}------{}$',
    '            ${}-----{}$',
    '             ${}---{}$',
    '              ${}-{}$',
    '               $-$',         
]
time.sleep(2)
rowIndex = 0


try:
    # This is the loop
    while True:
        # adds to rowIndex thus, creating a new line 
        rowIndex += 1
        # once the index is increased to the length of the row it
        # resets back to 0 thus, creating the animation.
        if rowIndex == len(rows):
            rowIndex = 0
        
        # row indexs 0 and 9 don't have nucleotides
        if rowIndex == 0 or rowIndex == 9:
            print(rows[rowIndex])
            continue

        # select random nucleotide pairs:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        print(rows[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(0.16)        
except KeyboardInterrupt:
    pass
