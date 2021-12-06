def binary_search(numbers, target_number):
    mid = len(numbers) // 2
    if target_number == numbers[mid]:
        return True
    if mid == 0:
        return False

    if target_number < numbers[mid]:
        return binary_search(numbers[:mid], target_number)
    elif target_number > numbers[mid]:
        return binary_search(numbers[mid:], target_number)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # 探索したい値
    target_number = 11
    # バイナリーサーチの実行
    print(binary_search(numbers, target_number))
