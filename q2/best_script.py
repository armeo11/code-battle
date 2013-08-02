from collections import Counter

def count_duplicate_numbers():
    counter = Counter()
    counter.update(line.strip() for line in open('numbers.txt').read().split())
    result = dict(counter)

    file_output = open('run_result.txt', 'w')
    file_output.writelines("%s \tis appear %s times\n" % (key, value) for key, value in result.items())

    file_output.close()

if __name__ == '__main__':
    count_duplicate_numbers()
