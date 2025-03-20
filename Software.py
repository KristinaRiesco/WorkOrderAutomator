#CustInfo
with open("TextFile.txt") as f:
    CustFirstName = f.write(input("Input customer's First Name: "))
    CustLastName = f.write(input("Input customer's last name: "))
    DeviceIssues = f.write(input("What are the issues with the device: "))
    deviceSymptoms = f.write(input("Are there any symptoms Y/N: "))
    if deviceSymptoms == 'Y':
        f.write(input("What are the symptoms: "))
    elif deviceSymptoms == 'y':
        f.write(input("What are the symptoms: "))
    deviceDamage = f.write(input("Was there preexisting damage Y/N: "))
    if deviceDamage == 'Y':
        f.write(input("What was the damage: "))
    elif deviceDamage == 'y':
        f.write(input("What was the damage: "))
    DeviceTestIssues = f.write(input("Were there any issues while testing the device Y/N: "))
    if DeviceTestIssues == 'Y':
        f.write(input("What were the issues while testing: "))
    elif DeviceTestIssues == 'y':
        f.write(input("What were the issues while testing: "))
    DeviceTestFailure = f.write(input("Were there any failures noticed when testing the device Y/N: "))
    if DeviceTestFailure == 'Y':
        f.write(input("What failures were noticed: "))
    elif DeviceTestFailure == 'y':
        f.write(input("What failures were noticed: "))

# device info
    DeviceBrand = f.write(input("Device Brand: "))
    DeviceModel = f.write(input("Device Model: "))
    DeviceColor = f.write(input("Color of device: "))
    DeviceAge = f.write(input("How hold is the device: "))
    DeviceIDNumber = input("Do you have the device ID or S/N number Y/N: ")
    if DeviceIDNumber == 'Y':
        f.write(input("Input device ID or S/N number: "))
    elif DeviceIDNumber == 'y':
        f.write(input("Input device ID or S/N number: "))
    else:
        f.write(input("State reason why: "))
    DevicePassword = f.write(input("Do you have the password for the device Y/N: "))
    if DevicePassword == 'Y':
        f.write(input("Input password for the device: "))
    elif DevicePassword == 'y':
        f.write(input("Input password for the device: "))
    else:
        f.write(input("State reason why: "))
    Depot = f.write(input("Will the device be sent to the depot Y/N: "))
    if Depot == 'N':
        f.write(input("Where will the device be held in Store: "))
    elif Depot == 'n':
        f.write(input("Where will the device be held in Store: "))
    AdditionalInfo = f.write(input("Note any additional Information here: "))
