def bubble_sort(list):
  for i in range(len(list)):
    for j in range(len(list)-1):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
  return list


list = [5,34,6,23,65,324,7,2,1]

print(bubble_sort(list))