# Utilizar um elemento como pivô e fazer a recursão
# tempo de execução: O(n log n)

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
print(quicksort([10, 5, 2, 3, 6, 8]))