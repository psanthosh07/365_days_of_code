def main():
    S = input()
    print(len(S))
    even=""
    #Print length of the string S
    print(S.index('a'))
    for i in range(len(S)):
        if i%2==0:
            even+=S[i]
           
    #Print the first occurence of the letter 'a' in S
    #Note it is guaranteed that letter a is present in the string S
    
    #Print all the characters with even index in S
    print(even)
    return 0

if __name__ == '__main__':
    main()
