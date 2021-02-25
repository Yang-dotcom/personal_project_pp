def main():
    try:
        with open("names.txt", "r") as file1:
            for i, line in enumerate(file1):
                temp_list = line.lower().split()
                if "ernesto" in temp_list and "giovanni" in temp_list:
                    print(f"Line {i+1}: {line}")
    except OSError as error:
        print(f"Error encountered: {error}")

if __name__ == '__main__':
    main()