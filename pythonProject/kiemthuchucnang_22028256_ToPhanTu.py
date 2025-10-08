def shipping_fee(weight, distance, hasVoucher=False):
    if weight <= 0 or weight > 50:
        return "Không giao được"

    if (distance < 1 or distance > 100):
        return "Khoảng cách không hợp lệ"

    if distance <= 5:
        fee = 20000
    elif distance <= 20:
        fee = 30000
    else:
        fee = 50000

    if hasVoucher:
        fee *= 0.8

    return int(fee)

def test_bva():
    cases = [
        # Test ID, w, d, hasVoucher, expected
        ("B1", 25, 50, True, 40000),
        ("B2", 25, 50, False, 50000),
        ("B3", 25, 1, True, 16000),
        ("B4", 25, 1, False, 20000),
        ("B5", 25, 2, True, 16000),
        ("B6", 25, 2, False, 20000),
        ("B7", 25, 99, True, 40000),
        ("B8", 25, 99, False, 50000),
        ("B9", 25, 100, True, 40000),
        ("B10", 25, 100, False, 50000),
        ("B11", 1, 50, True, 40000),
        ("B12", 1, 50, False, 50000),
        ("B13", 2, 50, True, 40000),
        ("B14", 2, 50, False, 50000),
        ("B15", 49, 50, True, 40000),
        ("B16", 49, 50, False, 50000),
        ("B17", 50, 50, True, 40000),
        ("B18", 50, 50, False, 50000),
    ]
    print("===== BVA Test Cases =====")
    for case in cases:
        tid, w, d, v, expected = case
        result = shipping_fee(w, d, v)
        print(f"{tid}: input=({w},{d},{v}) → result={result}, expected={expected} → {'PASS' if result==expected else 'FAIL'}")

def test_decision_table():
    cases = [
        # Rule, w, d, hasVoucher, expected
        ("R1", 0, 10, False, "Không giao được"),
        ("R2", 10, 3, False, 20000),
        ("R3", 10, 5, True, 16000),
        ("R4", 10, 10, False, 30000),
        ("R5", 10, 20, True, 24000),
        ("R6", 10, 50, False, 50000),
        ("R7", 10, 80, True, 40000),
        ("R8", 10, 120, False, "Khoảng cách không hợp lệ")
    ]
    print("\n===== Decision Table Test Cases =====")
    for case in cases:
        rid, w, d, v, expected = case
        result = shipping_fee(w, d, v)
        print(f"{rid}: input=({w},{d},{v}) → result={result}, expected={expected} → {'PASS' if result==expected else 'FAIL'}")

def test_decision_cases():
    cases = [
        ("D1", 90, 12, False, "Không giao được"),
        ("D2", 20, -3, False, "Khoảng cách không hợp lệ"),
        ("D3", 20, 3, True, 16000),
        ("D4", 20, 3, False, 20000),
        ("D5", 20, 15, False, 30000),
        ("D6", 20, 40, False, 50000),
    ]

    print("\n===== Decision Coverage (C2) Test Cases =====")
    for tid, w, d, v, expected in cases:
        result = shipping_fee(w, d, v)
        print(f"{tid}: input=({w},{d},{v}) → result={result}, expected={expected} → {'PASS' if result==expected else 'FAIL'}")


def main():
    test_bva()
    test_decision_table()
    test_decision_cases()

if __name__ == "__main__":
    main()