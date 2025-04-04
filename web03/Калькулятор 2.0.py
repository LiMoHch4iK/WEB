import sys

if len(sys.argv) > 1:
    try:
        print(sum(map(int, sys.argv[1::2])) - sum(map(int, sys.argv[2::2])))
    except Exception as e:
        print(type(e).__name__)
else:
    print('NO PARAMS')