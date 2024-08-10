def main(numbers):

  nums = list(set(numbers))

  nums.sort(reverse=True)

  return nums

if __name__ == "__main__":
  input_str = input("Enter numbers: ")
  numbers = [int(num) for num in input_str.split()]

  result = main(numbers)

  print(result)