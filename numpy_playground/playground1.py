import numpy as np

def question_1():
    """
    1. 创建一个从 0-9 的数组
    """
    print("Question 1:")
    # 选项 A
    arr_a = np.array(range(10))
    print("A:", arr_a)
    
    # 选项 B
    arr_b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("B:", arr_b)
    
    # 选项 C
    arr_c = np.arange(10)
    print("C:", arr_c)
    
    # 选项 D
    arr_d = np.array([i for i in range(10)])
    print("D:", arr_d)

def question_2():
    """
    2. 从数组中提取所有偶数
    """
    print("\nQuestion 2:")
    arr = np.arange(10)
    
    # 选项 A
    even_numbers = arr[arr % 2 == 0]
    print("A:", even_numbers)
    
    # 选项 B
    odd_numbers = arr[arr % 2 == 1]
    print("B:", odd_numbers)
    
    # 选项 C
    list_out = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            list_out.append(arr[i])
    even_numbers_c = np.array(list_out)
    print("C:", even_numbers_c)
    
    # 选项 D
    list_out = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            list_out.append(arr[i])
    odd_numbers_d = np.array(list_out)
    print("D:", odd_numbers_d)

def question_3():
    """
    3. 将数组中所有偶数替换为 -1
    """
    print("\nQuestion 3:")
    arr = np.arange(10)
    
    # 选项 A
    arr_a = arr.copy()
    arr_a[arr_a % 2 == 0] = -1
    print("A:", arr_a)
    
    # 选项 B
    arr_b = arr.copy()
    arr_b[arr_b % 2 == 0] = -1
    print("B:", arr_b)
    
    # 选项 C
    arr_c = np.where(arr % 2 == 1, -1, arr)
    print("C:", arr_c)
    
    # 选项 D
    arr_d = np.where(arr % 2 == 1, -1, arr)
    print("D:", arr_d)

def question_4():
    """
    4. 数组形状操作
    """
    print("\nQuestion 4:")
    arr = np.arange(10)
    
    # 选项 A
    print("A: Array shape is", arr.shape)
    
    # 选项 B
    reshaped_b = np.reshape(arr, [2, 5])
    print("B:", reshaped_b)
    
    # 选项 C
    reshaped_c = np.reshape(arr, (2, 5))
    print("C:", reshaped_c)
    
    # 选项 D
    reshaped_d = np.reshape(arr, [2, 5])
    print("D:", reshaped_d)

def question_5():
    """
    5. 数组拼接
    """
    print("\nQuestion 5:")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [10, 11, 12]])
    
    # 选项 A
    vstack_result = np.vstack((a, b))
    print("A:", vstack_result.shape)
    
    # 选项 B
    hstack_result = np.hstack((a, b))
    print("B:", hstack_result.shape)

def question_6():
    """
    6. 数组交集
    """
    print("\nQuestion 6:")
    a = np.array([1, 2, 3, 4])
    b = np.array([3, 4, 5, 6])
    
    # 选项 C
    intersect = np.intersect1d(a, b)
    print("C:", intersect)

def question_7():
    """
    7. 数组差集
    """
    print("\nQuestion 7:")
    a = np.array([1, 2, 3, 4])
    b = np.array([3, 4, 5, 6])
    
    # 选项 C
    diff = np.setdiff1d(a, b)
    print("C:", diff)

def question_8():
    """
    8. 条件筛选
    """
    print("\nQuestion 8:")
    arr = np.arange(10)
    
    # 选项 D
    filtered = arr[(arr >= 5) & (arr <= 10)]
    print("D:", filtered)

def question_9():
    """
    9. 数组行交换
    """
    print("\nQuestion 9:")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # 选项 A
    swapped = arr[[1, 0, 2], :]
    print("A:", swapped)

def question_10():
    """
    10. 数组值裁剪
    """
    print("\nQuestion 10:")
    arr = np.array([5, 15, 25, 35])
    
    # 选项 A
    arr[arr > 20] = 20
    arr[arr < 10] = 10
    print("A:", arr)
    
    # 选项 B
    clipped = np.clip(arr, 10, 20)
    print("B:", clipped)

def question_11():
    """
    11. 数组最大值位置
    """
    print("\nQuestion 11:")
    np.random.seed(100)
    arr = np.random.uniform(1, 20, 10)
    
    max_value = np.max(arr)
    max_index = np.where(arr == max_value)
    print("A: Max value index is", max_index)

def question_12():
    """
    12. 数组展平
    """
    print("\nQuestion 12:")
    arr = np.array([[1, 2], [3, 4]])
    
    # 选项 A
    flattened_a = arr.flatten()
    print("A:", flattened_a)
    
    # 选项 B
    flattened_b = arr.reshape(-1)
    print("B:", flattened_b)

def question_13():
    """
    13. 数组元素计数
    """
    print("\nQuestion 13:")
    np.random.seed(150)
    arr = np.random.randint(1, 11, size=(6, 10))
    
    res = []
    for i in arr:
        temp = []
        for j in range(1, 11):
            temp.append(np.count_nonzero(i == j))
        res.append(temp)
    print("A:", res)

def question_14():
    """
    14. 数组每行最大值
    """
    print("\nQuestion 14:")
    np.random.seed(150)
    arr = np.random.randint(1, 10, size=(5, 3))
    
    max_values = np.max(arr, axis=1)
    print("A:", max_values)

def question_15():
    """
    15. 数组每行最大值位置
    """
    print("\nQuestion 15:")
    np.random.seed(150)
    arr = np.random.randint(1, 10, size=(5, 3))
    
    max_indices = np.argmax(arr, axis=1)
    print("C:", max_indices)

def question_16():
    """
    16. 数组去重
    """
    print("\nQuestion 16:")
    arr = np.array([1, 1, 2, 3, 4, 4, 5, 5, 5])
    
    unique_values, indices = np.unique(arr, return_index=True)
    print("A:", unique_values)

def question_17():
    """
    17. 删除数组中的 NaN 值
    """
    print("\nQuestion 17:")
    arr = np.array([1, 2, 5, 3, 8, np.nan, 5, 5, 8, 0])
    
    nan_indices = np.isnan(arr)
    cleaned_arr = np.delete(arr, np.where(nan_indices))
    print("C:", cleaned_arr)

def question_18():
    """
    18. 数组广播
    """
    print("\nQuestion 18:")
    a = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
    b = np.array([1, 1, 1])
    
    result = a - b
    print("A:", result)

def question_19():
    """
    19. 数组广播结果
    """
    print("\nQuestion 19:")
    a = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
    b = np.array([1, 1, 1])
    
    result = a - b
    print("A:", result)

def question_20():
    """
    20. 数组元素计数
    """
    print("\nQuestion 20:")
    x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
    
    temp = 0
    for index, val in enumerate(x):
        if val == 1:
            temp += 1
        if temp == 6:
            print("B:", index)
            break

def main():
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
    question_6()
    question_7()
    question_8()
    question_9()
    question_10()
    question_11()
    question_12()
    question_13()
    question_14()
    question_15()
    question_16()
    question_17()
    question_18()
    question_19()
    question_20()

if __name__ == "__main__":
    main()
