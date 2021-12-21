import sys

def mapper():
    """
    Parses "UNIT" and "ENTRIESn_hourly" for each row and prints to stdout
    """
    next(sys.stdin)
    for line in sys.stdin:
        observation = line.strip().split(",")
        
        if len(observation) >= 4:
            unit = observation[0]
            entriesn_hourly = observation[2]
            print "%s\t%s" % (unit, entriesn_hourly)

sys.stdin = open('/Users/Damon/Desktop/csc485B/Assignment/ml-latest-small/ratings.csv')
sys.stdout = open('mapper_result.txt', 'w')
mapper()

def reducer():
    """
    Reads mapper result from stdin and prints "UNIT" and total hourly entries \
    for that unit
    Since UNIT appear at multiple lines in mapper result, we will take sum of \
    all entries for each UNIT
    """
    old_key = None
    entries_count = 0

    for line in sys.stdin:
        
        row = line.strip().split("\t")
        
        if len(row) != 2:
            continue
        
        this_key, this_entry = row
       
        try:
            for key in this_key:
            if (old_key) and (old_key != this_key):
                entries_count = entries_count/this_c
                print "%s\t%s" % (old_key, entries_count)
                old_key = this_key
                entries_count = 0
            old_key = this_key
            entries_count += float(this_entry)
 

        except:
            continue
    
    #print "%s\t%s" %(old_key, entries_count)
        
sys.stdin = open('mapper_result.txt')
sys.stdout = open('reducer_result.txt', 'w')
reducer()