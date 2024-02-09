def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm', 'allows', 'community', 'phase', 'single']
    my_list = []
    my_list=[x for x in (str_list) if len(x)%2==1]
    print(my_list)
    return 0

if __name__ == '__main__':
    main()
