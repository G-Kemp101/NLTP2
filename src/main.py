from nltp import nltp

def main():
    compiler = nltp()
    while(True):
        line = input('>>> ')
        compiler.compile(line)


if __name__ == "__main__":
    main()