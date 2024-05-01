if __name__ == "__main__":
  # Introduction to Python try…catch…finally statement

  """
  try:
    # code that may cause exceptions
  except:
    # code that handle exceptions
  finally:
    # code that clean up
  """

  # Python try…catch…finally statement examples

  a = 10
  b = 0

  try:
    c = a / b
    print(c)
  except ZeroDivisionError as error:
    print(error)
  finally:
    print("Finishing up.")

  # Python try…finally statement

  """
  try:
    # the code that may cause an exception
  finally:
    # the code that always executes
  """
