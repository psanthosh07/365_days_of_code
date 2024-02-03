def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    a=list(tuple1)
    b=list(tuple2)
    a[0]="number"
    b[0]="number"
    tuple1=tuple(a)
    tuple2=tuple(b)
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    
    
    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()
