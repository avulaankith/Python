import copy
import math


def calculate_cost(x, y):
    cost_list = []
    for i in range(3):
        for j in range(3):
            cost_list.append(finding_nemo(y, x[i][j], i, j))
    return cost_list


def finding_nemo(x, ele, n, m):
    for i in range(3):
        for j in range(3):
            if x[i][j] == ele:
                xcoeff = (i - n)
                ycoeff = (j - m)
                if xcoeff < 0:
                    xcoeff = -xcoeff
                if ycoeff < 0:
                    ycoeff = -ycoeff
                res = xcoeff + ycoeff
                return (res)


def find_coordinates(l, x, y, cost_list):
    m = min(i for i in cost_list if i > 0)
    ele = cost_list.index(m)
    ele = l[ele]
    print(ele)
    for i in range(3):
        for j in range(3):
            if ele == x[i][j]:
                return (i, j)


def start_movement(n, m):
    tm = 4
    if n == 0 or n == 2:
        tm -= 1
    if m == 0 or m == 2:
        tm -= 1
    print(f"The total possible moves for the tile ({n},{m}) are: {tm}")


def move_down(ma, y, n, m, costl):
    x = ma
    cost_s = 100000
    print("The block moved down!!!")
    if n != 2:
        x[n][m], x[n + 1][m] = x[n + 1][m], x[n][m]
        m1 = x
        print(m1)
        costl = calculate_cost(m1, final_copy)
        cost_s = sum(costl)
        print(calculate_cost(m1, final_copy))
    # if n == 1:
    #     x[n][m], x[n + 1][m] = x[n + 1][m], x[n][m]
    #     m1 = x
    #     print(m1)
    #     print(calculate_cost(m1, final_copy))
    return costl, cost_s


def move_up(ma, y, n, m, costl):
    x = ma
    cost_s = 100000
    print("The block moved up!!!")
    if n != 0:
        x[n - 1][m], x[n][m] = x[n][m], x[n - 1][m]
        m2 = x
        print(m2)
        costl = calculate_cost(m2, final_copy)
        cost_s = sum(costl)
        print(calculate_cost(m2, final_copy))
    # if n == 1:
    #     x[n - 1][m], x[n][m] = x[n][m], x[n - 1][m]
    #     m2 = x
    #     print(m2)
    #     print(calculate_cost(m2, final_copy))
    return costl, cost_s


def move_left(ma, y, n, m, costl):
    x = ma
    cost_s = 100000
    print("The block moved left!!!")
    if m != 0:
        x[n][m - 1], x[n][m] = x[n][m], x[n][m - 1]
        m2 = x
        print(m2)
        costl = calculate_cost(m2, final_copy)
        cost_s = sum(costl)
        print(calculate_cost(m2, final_copy))
    # if m == 1:
    #     x[n][m - 1], x[n][m] = x[n][m], x[n][m - 1]
    #     m2 = x
    #     print(m2)
    #     print(calculate_cost(m2, final_copy))
    return costl, cost_s


def move_right(ma, y, n, m, costl):
    x = ma
    cost_s = 100000
    print("The block moved right!!!")
    if m != 2:
        x[n][m + 1], x[n][m] = x[n][m], x[n][m + 1]
        m2 = x
        print(m2)
        costl = calculate_cost(m2, final_copy)
        cost_s = sum(costl)
        print(calculate_cost(m2, final_copy))
    # if m == 1:
    #     x[n][m + 1], x[n][m] = x[n][m], x[n][m + 1]
    #     m2 = x
    #     print(m2)
    #     print(calculate_cost(m2, final_copy))
    return costl, cost_s


final_square = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
final_copy = copy.deepcopy(final_square)
initial_square = []
spare_sqaure = []
# l = [int(i) for i in input().split()]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
m = 0
for i in range(3):
    initial_square.append(l[m:n])
    spare_sqaure.append(l[m:n])
    n += 3
    m += 3
copy1 = copy.deepcopy(initial_square)
copy2 = copy.deepcopy(initial_square)
copy3 = copy.deepcopy(initial_square)
copy4 = copy.deepcopy(initial_square)
cost_list = calculate_cost(initial_square, final_square)
n, m = find_coordinates(l, initial_square, final_square, cost_list)
print(l)
print(calculate_cost(initial_square, final_square))
cost_list = calculate_cost(initial_square, final_square)
cost_sum = sum(cost_list)
print(find_coordinates(l, initial_square, final_square, cost_list))
while cost_sum > 0:
    print(start_movement(n, m))
    cl1, cost1 = move_down(copy1, final_copy, n, m, cost_list)
    cl2, cost2 = move_up(copy2, final_copy, n, m, cost_list)
    cl3, cost3 = move_left(copy3, final_copy, n, m, cost_list)
    cl4, cost4 = move_right(copy4, final_copy, n, m, cost_list)
    if cost1 <= cost_sum and cost1 == min(cost1, cost2, cost3, cost4):
        cost_sum = cost1
        cost_list = cl1
        copy1 = copy.deepcopy(copy1)
        copy2 = copy.deepcopy(copy1)
        copy3 = copy.deepcopy(copy1)
        copy4 = copy.deepcopy(copy1)
    elif cost2 <= cost_sum and cost2 == min(cost1, cost2, cost3, cost4):
        cost_sum = cost2
        cost_list = cl2
        copy1 = copy.deepcopy(copy2)
        copy2 = copy.deepcopy(copy2)
        copy3 = copy.deepcopy(copy2)
        copy4 = copy.deepcopy(copy2)
    elif cost3 <= cost_sum and cost3 == min(cost1, cost2, cost3, cost4):
        cost_sum = cost3
        cost_list = cl3
        copy1 = copy.deepcopy(copy3)
        copy2 = copy.deepcopy(copy3)
        copy3 = copy.deepcopy(copy3)
        copy4 = copy.deepcopy(copy3)
    elif cost4 <= cost_sum and cost4 == min(cost1, cost2, cost3, cost4):
        cost_sum = cost4
        cost_list = cl4
        copy1 = copy.deepcopy(copy4)
        copy2 = copy.deepcopy(copy4)
        copy3 = copy.deepcopy(copy4)
        copy4 = copy.deepcopy(copy4)
    n, m = find_coordinates(l, copy1, final_square, cost_list)
    print(find_coordinates(l, copy1, final_square, cost_list))
