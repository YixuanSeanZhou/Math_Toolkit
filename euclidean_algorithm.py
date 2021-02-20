import sys
import getopt

def euclidean_algorithm_gcd(a, b):
    if (a < b):
        temp = b
        b = a
        a = temp

    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        q = old_r // r
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
        (old_t, t) = (t, old_t - q * t)

    ret = {
        'input': (a, b),
        'gcd': old_r,
        'Bézout coefficients': (old_s, old_t),
        'quotients by the gcd:': (t, s)
    }

    return ret


if __name__ == '__main__':
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "ha:b:", ["num_a=", "num_b="])
    except getopt.GetoptError:
        print('euclidean_algorithm.py -a <input_num_a> -b <input_num_b>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('euclidean_algorithm.py -a <input_num_a> -b <input_num_b>')
            sys.exit()
        elif opt in ("-a", "--num_a"):
            try:
                num_a = int(arg)
            except:
                print('Input should be int')
        elif opt in ("-b", "--num_b"):
            try:
                num_b = int(arg)
            except:
                print('Input should be int')

    ret = euclidean_algorithm_gcd(num_a, num_b)
    print(ret)

