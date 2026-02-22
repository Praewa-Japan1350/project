def alternate(s):
    unique_chars = list(set(s))
    max_length = 0

    # ลองจับคู่ตัวอักษรทีละ 2 ตัว
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]

            # กรอง string ให้เหลือแค่ 2 ตัวนี้
            filtered = [c for c in s if c == char1 or c == char2]

            # เช็คว่าสลับกันจริงไหม
            valid = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k + 1]:
                    valid = False
                    break

            if valid and len(filtered) > 1:
                max_length = max(max_length, len(filtered))

    return max_length