import sys

def mapper():
    """
    Parses "UNIT" and "ENTRIESn_hourly" for each row and prints to stdout
    """
    next(sys.stdin)
    for line in sys.stdin:
        observation = line.strip().split(",")
        
        if len(observation) >= 7:
            unit = observation[1]
            entriesn_hourly = observation[6]
            print "%s\t%s" % (unit, entriesn_hourly)

sys.stdin = open('/Users/Damon/Desktop/csc485B/Assignment/ml-latest-small/ratings.csv')
sys.stdout = open('mapper_result.txt', 'w')
mapper()