import os
import heapq

def sort(list): 
    if len(list) > 1: 
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]
        i = j = k = 0
        sort(L)
        sort(R)
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

def merge(*lists):
    return heapq.merge(*lists)
    
num_of_files = list()
dir_path = os.getcwd()
input_path = os.path.join(dir_path,'input')
for filename in os.listdir(input_path):
    input_file = input_path + '/' + filename
    with open(input_file) as file:
        num_of_file = list()
        for line in file:
            num_of_file.append(int(line.strip("\n"),10))
        sort(num_of_file)
        num_of_files.append(num_of_file)
    file.close()
kway = list(merge(*num_of_files))
output_path = os.path.join(dir_path, 'output')
if not os.path.exists(output_path):
    os.mkdir(output_path)
output_file = output_path + '/sorted.txt'
for num in kway:
    with open(output_file, 'w+') as file:
        for num in kway:
            file.write(str(num) + '\n')
    file.close()