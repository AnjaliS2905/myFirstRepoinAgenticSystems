with open("numbers.txt","r") as file:
    lines=file.readlines()
    print(f"Read {len(lines)} numbers") 
    list=[int(i.strip("\n")) for i in lines ]
    print(f"Sum:",sum(list))
    avg=sum(list)/len(list) if len(list)> 0 else 0
    print("Average:",avg)
    print("Processing Completed")
with open("results.log.","a") as logger:
    logger.write("File Opened\n")
    logger.write("Data Loaded\n")
    logger.write("Computation Completed")
   