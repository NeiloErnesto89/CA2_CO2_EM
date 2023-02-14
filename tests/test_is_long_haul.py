from CodeToTest import is_long_haul

def test_is_long_haul() -> None:
    long_haul = is_long_haul("Test")
    assert long_haul
    
    