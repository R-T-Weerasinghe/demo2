def login():
  u = input("Enter your username")
  p = input("Enter your password")
  if u=="admin" and p=="admin123":
    return True
  return False
