class Participants:
    def __init__(self, login, score, penalty):
        self.login = login
        self.score = int(score)
        self.penalty = int(penalty)

    def __eq__(self, other):
        return self == other

    def __gt__(obj1, obj2):
        return not(obj1.score > obj2.score or obj1.score == obj2.score and (obj1.penalty < obj2.penalty or obj1.penalty == obj2.penalty and obj1.login < obj2.login))

    def __lt__(obj1, obj2):
        return obj1.score > obj2.score or obj1.score == obj2.score and (obj1.penalty < obj2.penalty or obj1.penalty == obj2.penalty and obj1.login < obj2.login)


def quicksort(arr, left, right):
    if right - left > 1:
        elem = partition(arr, left, right)
        quicksort(arr, left, elem)
        quicksort(arr, elem + 1, right)

def partition(arr, left, right):
    pivot = arr[left]
    l = left + 1
    r = right - 1
    while True:
        while l <= r and arr[l] < pivot:
            l += 1
        while l <= r and arr[r] > pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
        elif l > r:
            arr[left], arr[r] = arr[r], arr[left]
            return r

def main():
    n = int(input())
    arr = []
    for i in range(n):
        login, completed_task, penalty = input().split()
        objects = Participants(login, completed_task, penalty)
        arr.append(objects)

    quicksort(arr, 0, n)

    for i in range(n):
        print(arr[i].login)

if __name__ == '__main__':
    main()
