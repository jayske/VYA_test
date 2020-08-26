import vya_luhn as luhn
verbose = True
#-----------------------------------#
# UNIT TESTING for LUHN #
def runemall():
    # a simple script to try all the tests
    count = 1
    passed = 1
    failed = 1
    for t in all_of_em:
        print('Passed:', passed, 'test out of', count)
        count += 1
        passed += 1

    print('Total tests:', count, 'Tests passed:', passed)
    print('-------------------------------------------')
    print('*** testing complete ***')

def test_0():
    input=['0','0']
    expected = 0
    result = luhn.do_luhn(input)
    assert result==expected, 'sum of 0 and 0 is 0'

def test_1():
    input=['1','2','1']
    expected = 6
    result = luhn.do_luhn(input)
    assert result==expected, 'because (2 * 2 = 4) which is < 9 so 1 + 4 + 1 = 6'

def test_2():
    input=['1','9','1']
    expected = 11
    result = luhn.do_luhn(input)
    assert result==expected, 'because (9 * 2 = 18) which is > 9 so 1 + 1 + 8 + 1 = 11'

def test_3():
    input=['1','2','1','2']
    expected = 10
    result = luhn.do_luhn(input)
    assert result==expected, 'because (2 * 2 = 4) which is < 9 so 1 + 4 + 1 + 4 = 10'

def test_4():
    input=['1','9','1','9']
    expected = 20
    result = luhn.do_luhn(input)
    assert result==expected, 'because (9 * 2 = 18) which is > 9 so 1 + 1 + 8 + 1 + 1+ 8 = 20'

def test_5():
    input=['-1','2']
    expected = -1
    result = luhn.do_luhn(input)
    assert result==expected, 'credit card number cannot be negative'
# ----------------------------------------------------------------------------------------------
# UNIT TESTING for sum_luhn
def test_6():
    input= 10000
    expected = "the number is valid"
    result = luhn.sum_luhn(input)
    assert result==expected, ' 10000 % 10 = 0'

def test_7():                                                      
    input= 5
    expected = "the number is invalid"
    result = luhn.sum_luhn(input)
    assert result==expected, '5 % is not 0'

# ------------------------------------------------------------------------------------------------
# INTERGRATING TEST
def test_8():
    input = luhn.do_luhn(['1','9','1','9'])
    expected = "the number is valid"
    result = luhn.sum_luhn(input)
    assert result==expected, ' 20 % 10 = 0'

def test_9():
    input= luhn.do_luhn(['0','0'])
    expected = "the number is valid"
    result = luhn.sum_luhn(input)
    assert result==expected, ' 0 % 10 = 0'

def test_10():
    input= luhn.do_luhn(['1','9','1'])
    expected = "the number is invalid"
    result = luhn.sum_luhn(input)
    assert result==expected, ' 11 % 10 != 0'

def test_11():
    input= luhn.do_luhn(['-1','2'])
    expected = "the number is invalid"
    result = luhn.sum_luhn(input)
    assert result==expected, 'sum returns -1'

def test_12():
    input= luhn.do_luhn([3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6])
    expected = "the number is valid"
    result = luhn.sum_luhn(input)
    assert result==expected, 'this is a valid credit card number'

def test_13():
    input= luhn.do_luhn([5, 0, 9, 2, 8, 6, 0, 4, 3, 4, 4, 1, 1, 1, 0, 6])
    expected = "the number is valid"
    result = luhn.sum_luhn(input)
    assert result==expected, 'this is a valid credit card number'   

def test_14():
    input= luhn.do_luhn([5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3])
    expected = "the number is valid"
    result = luhn.sum_luhn(input)
    assert result==expected, 'this is a invalid credit card number'

def test_15():
    input= luhn.do_luhn([3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4])
    expected = "the number is invalid"
    result = luhn.sum_luhn(input)
    assert result==expected, 'this is a invalid credit card number'


all_of_em = [ test_0,
              test_1(),
              test_2(),
              test_3(),
              test_4(),
              test_5(),
              test_6(),
              test_7(),
              test_8(),
              test_9(),
              test_10(),
              test_11(),
              test_12(),
              test_13(),
              test_14(),
              test_15()
            ]
runemall()