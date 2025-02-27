from first.nums import plus

if __name__== "__main__":
  print(plus(3, 3))
  print("Hello")
  test = input(f"Text n+n")
  left, right = test.split("+")
  left, right = int(left), int(right)
  print(left + right)