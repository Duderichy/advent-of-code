from functools import reduce
import operator

def main():
    with open("02data.txt") as data:
        for line in data:
            array = list([int(x) for x in line.split(',')])
            array[1] = 12
            array[2] = 2
            return computer(array)

def main2():
    with open("02data.txt") as data:
        for line in data:
            start_array = list([int(x) for x in line.split(',')])
    count = 0
    for i in range(100):
        for j in range(100):
            count += 1
            array = start_array[:]
            array[1] = i
            array[2] = j
            if count % 1000 == 0 or i == 0 and j == 0:
                print(count)
                print(array)
            if i == 50 and j == 50:
                print("FOO")
                print(array)
                print("BAR")
                print(start_array)
            output = computer(array)
            if output == 3101844 or i == 12 and j == 2:
                print("YOU FOUND ME HERE")
                print("YOU FOUND ME HERE")
                print(i, j, output)
                print("YOU FOUND ME HERE")
                print("YOU FOUND ME HERE")
            if output[0] == 19690720:
                print("HOORAY!!")
                print("HOORAY!!")
                print("HOORAY!!")
                print("HOORAY!!")
                print("HOORAY!!")
                return i, j

def computer(array):
    pos = 0
    ret_pos = 0
    opcode = {
        1 : operator.add ,
        2 : operator.mul ,
    }
    while array[pos] != 99:
        oper = opcode[array[pos]]
        # print(pos, oper)
        result = reduce(oper, [array[array[pos + 1]], array[array[pos + 2]]])
        # print('pos', pos, ',', 'res', result, end = ', ')
        array[array[pos + 3]] = result
        pos += 4
    else:
        # print()
        return array[ret_pos], array

if __name__ == "__main__":
    print(computer([1,0,0,0,99]))
    print(computer([2,3,0,3,99]))
    print(computer([2,4,4,5,99,0]))
    print(computer([2,4,4,5,99,0]))
    print(computer([1,1,1,4,99,5,6,0,99]))
    print(computer([1,9,10,3,2,3,11,0,99,30,40,50]))
    print(main())
    print(main2())
