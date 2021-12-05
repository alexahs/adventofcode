
def find_seat(seat_nums):
    
    rows = list(range(128)) 
    seats = list(range(8))

    for i, s in enumerate(seat_nums):
        if s == "F":
            rows = rows[:len(rows)//2]
        elif s == "B":
            rows = rows[len(rows)//2:]
        elif s == "L":
            seats = seats[:len(seats)//2]
        elif s == "R":
            seats = seats[len(seats)//2:]

    return 8*rows[0] + seats[0]



def main():
    with open("input.txt", "r") as fp:
        data = list(map(str.strip, fp.readlines()))

    seat_list = []
    for seat_nums in data:
        seat_list.append(find_seat(seat_nums))
    

    s_list = sorted(seat_list)

    num = s_list[1]
    for i in range(2, len(s_list)):
        if s_list[i] != (num + 1):
            print(f"seat num: {s_list[i]}")
            num += 1
        num += 1




if __name__ == '__main__':
    main()
