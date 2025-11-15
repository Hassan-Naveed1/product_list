def product(product_list):

  result = 1

  for i in range(len(product_list)):
    result = result * product_list[i]
  return result

print(product([4,5,5]))