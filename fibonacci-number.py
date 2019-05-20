#python3


def fibonacci(n):
    """
    Fibinocci using an array to optimize the solution
    Time complexity: O(2n + 2) ~= O(n)
    :param n: integer
    :return: fibinocci value of nth number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    feb_n = [0, 1]
    for num in range(2, n):
        feb_n.append(feb_n[num - 1] + feb_n[num - 2])
    return feb_n[n-1]


if __name__ == '__main__':
    print(fibonacci(20))
