import pandas as pd
import h5py
import numpy as np


def h5py_method():
    # 開きたいファイルのパス
    path = './csv/4080_data_handling_data/population.hdf5'

    # ファイルを開く
    # 'r'は読み取りモードの意味
    population_data = h5py.File(path, 'r')
    for prefecture in population_data.keys():
        for city in population_data[prefecture].keys():
            for i in population_data[prefecture][city].keys():
                print(type(population_data[prefecture][city][i]))
                print(prefecture + '県' + city + '市' + i + '丁目: ', population_data[prefecture][city][i])
    # 閉じる
    population_data.close()



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
    # print(binary_search(numbers, target_number))
    print()
