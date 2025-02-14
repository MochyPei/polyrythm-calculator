def calculate_polyrhythm(value, divisions, mode):
    return {d: value * d for d in divisions}

def calculate_relative_polyrhythm(value, current_division, divisions, mode):
    base_value = value / current_division
    return {d: base_value * d for d in divisions}

def parse_divisions(input_str):
    divisions = list(map(int, input_str.split()))
    if len(divisions) == 1:
        return list(range(1, divisions[0] + 1))
    return sorted(set(divisions))

def main():
    while True:
        print("\nПолиритмический калькулятор")
        print("1. Рассчитать полиритм в BPM")
        print("2. Рассчитать полиритм в Гц")
        print("3. Рассчитать полиритм от заданного деления в BPM")
        print("4. Рассчитать полиритм от заданного деления в Гц")
        print("5. Выйти")
        
        choice = input("Выбери действие (1-5): ")
        
        if choice == "1":
            bpm = float(input("Введите BPM: "))
            divisions = parse_divisions(input("Введите деления (одно число для всех или несколько через пробел): "))
            results = calculate_polyrhythm(bpm, divisions, "BPM")
            
            for d, r in results.items():
                print(f"{d}: {r:.2f} BPM")
        
        elif choice == "2":
            hz = float(input("Введите частоту (Гц): "))
            divisions = parse_divisions(input("Введите деления (одно число для всех или несколько через пробел): "))
            results = calculate_polyrhythm(hz, divisions, "Hz")
            
            for d, r in results.items():
                print(f"{d}: {r:.2f} Гц")
        
        elif choice == "3":
            bpm = float(input("Введите частоту в BPM: "))
            current_division = int(input("Введите текущее деление: "))
            divisions = parse_divisions(input("Введите необходимые деления (одно число для всех или несколько через пробел): "))
            results = calculate_relative_polyrhythm(bpm, current_division, divisions, "BPM")
            
            for d, r in results.items():
                print(f"{d}: {r:.2f} BPM")
        
        elif choice == "4":
            hz = float(input("Введите частоту в Гц: "))
            current_division = int(input("Введите текущее деление: "))
            divisions = parse_divisions(input("Введите необходимые деления (одно число для всех или несколько через пробел): "))
            results = calculate_relative_polyrhythm(hz, current_division, divisions, "Hz")
            
            for d, r in results.items():
                print(f"{d}: {r:.2f} Гц")
        
        elif choice == "5":
            print("Выход...")
            break
        
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
