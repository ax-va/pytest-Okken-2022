def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

# Run pytest in the terminal:
# $ pytest test_example-01-1-passing.py
# ===================================================================================================== test session starts ======================================================================================================
# ###
# collected 1 item
#
# test_example-01-1-passing.py .                                                                                                                                                                                                      [100%]
#
# ====================================================================================================== 1 passed in 0.00s =======================================================================================================

# $ pytest -v test_example-01-1-passing.py
# ===================================================================================================== test session starts ======================================================================================================
# ###
# collected 1 item
#
# test_example-01-1-passing.py::test_passing PASSED                                                                                                                                                                                   [100%]
#
# ====================================================================================================== 1 passed in 0.00s =======================================================================================================
