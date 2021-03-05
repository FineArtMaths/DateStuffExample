months = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]

leapYears = []
for y in range(1, 2001):
  addit = False
  if y % 100 == 0:
    if y % 400 == 0:
      addit = True
  elif y % 4 == 0:
    addit = True

  if addit:
    leapYears.append(y)