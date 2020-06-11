from nltp import nltp

def main():
    compiler = nltp()
    compiler.compile("add the worst student to the average student")
    # while(True):
    #     line = input('>>> ')
    #     compiler.compile(line)


if __name__ == "__main__":
    main()