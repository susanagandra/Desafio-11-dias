#Crie um programa que funcione como um temporizador (contagem progressiva) ou contador regressivo. 
#O usuário vai poder escolher entre as duas opções.


import time

def timer(time_limit, countdown=True):
    if countdown:
        while time_limit > 0:
            print(f"Time remaining: {time_limit} seconds")
            time.sleep(1)
            time_limit -= 1
    else:
        for seconds in range(time_limit + 1):
            print(f"Elapsed time: {seconds} seconds")
            time.sleep(1)

def main():
    choice = input("Choose 'P' for progressive counting or 'R' for countdown: ").upper()

    if choice == 'P':
        total_time = int(input("Enter the total seconds for progressive counting: "))
        timer(total_time, False)
    elif choice == 'R':
        total_time = int(input("Enter the total seconds for countdown: "))
        timer(total_time)
    else:
        print("Invalid choice. Please select 'P' or 'R'.")

if __name__ == "__main__":
    main()
