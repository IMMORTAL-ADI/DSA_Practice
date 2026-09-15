def memory(count):
    if count == 4:
        return 
    count+=1
    print("Hello")
    memory(count)
    return
if __name__ == "__main__":
    memory(0)