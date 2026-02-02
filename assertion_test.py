try:
    id_1 = 1 
    id_2 = 2 
    id_3 = 3 
    assert (id_1 < id_2 < id_3 == 3)
except AssertionError as e:
    print(f"there was an assertion error {e}")
