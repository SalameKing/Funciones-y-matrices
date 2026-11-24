while True:
    print ("Bienvenido al Gestor de Contraseñas. Por favor, seleccione una opción del menú:")
    print("\n=== Gestor de contraseñas ===")
    print("1. Generar contraseña segura recomendada")
    print("2. Evaluar fortaleza de una contraseña")
    print("3. Guardar una contraseña en la bóveda")
    print("4. Ver contraseñas guardadas")
    print("0. Salir")

    input_option = input("Ingrese el número de la opción deseada: ")
    if input_option == "1":
        from gestor.password_generator import generate_password
        password = generate_password()
        print(f"Contraseña generada: {password}")
    elif input_option == "2":
        from password_strength import evaluate_password_strength
        password_to_evaluate = input("Ingrese la contraseña a evaluar: ")
        strength = evaluate_password_strength(password_to_evaluate)
        print(f"La fortaleza de la contraseña es: {strength}")
    elif input_option == "3":
        from password_vault import save_password
        password_to_save = input("Ingrese la contraseña a guardar: ")
        save_password(password_to_save)
        print("Contraseña guardada exitosamente.")
    elif input_option == "4":
        from password_vault import view_saved_passwords
        saved_passwords = view_saved_passwords()
        print("Contraseñas guardadas:")
        for idx, pwd in enumerate(saved_passwords, start=1):
            print(f"{idx}. {pwd}")
    elif input_option == "0":
        print("Saliendo del Gestor de Contraseñas. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")