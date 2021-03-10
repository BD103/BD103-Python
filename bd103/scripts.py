def repeat(cycles, func):
  if not callable(func):
    raise ValueError("func parameter is not callable")
  else:
    for i in range(cycles):
      func()