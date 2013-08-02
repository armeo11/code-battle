def report_missing_numbers():
    numbers = set('%04d' % x for x in range(10000))
    numbers_in_file = set(line.strip() for line in open('numbers.txt'))
    missing_numbers = numbers - numbers_in_file

    file_output = open('run_result.txt', 'w')
    file_output.writelines("%s\n" % item for item in missing_numbers)

    file_output.close()

if __name__ == '__main__':
    report_missing_numbers()
