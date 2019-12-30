import os


def main():
    pyfiles = []
    files = os.listdir('.')
    for file in files:
        if file.endswith('.py'):
            mdName = file.replace('.py', '.md')
            if mdName in files:
                continue
            


if __name__ == "__main__":
    main()