# 1
def smfunc1(a, b):
  return a + b

def test_func():
  assert 0 == smfunc1(0, 0)
  assert 4 == smfunc1(2, 2)

# 2 
def smfunc2(a, b):
    return a ** b

#add 2 in the end of the method 
def test_func2():
    assert 1 == smfunc2(1, 1)
    assert 4 == smfunc2(2, 2)
    
# Insert main function to except error
if __name__ == "__main__":
    test_func()
    test_func2
    print("Tests passed")
