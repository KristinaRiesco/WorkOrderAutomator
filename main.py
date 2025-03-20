with open('customer_device_info.txt', 'w') as file:
    # CustInfo
    CustFirstName = input("Input customer's First Name: ")
    CustLastName = input("Input customer's last name: ")
    file.write(f"Customer's First Name: {CustFirstName}\n")
    file.write(f"Customer's Last Name: {CustLastName}\n")

    # Pre-Test
    DeviceIssues = input("What are the issues with the device: ")
    file.write(f"Issues with the device: {DeviceIssues}\n")

    deviceSymptoms = input("Are there any symptoms Y/N: ")
    if deviceSymptoms.lower() == 'y':
        symptoms = input("What are the symptoms: ")
        file.write(f"Symptoms: {symptoms}\n")

    deviceDamage = input("Was there preexisting damage Y/N: ")
    if deviceDamage.lower() == 'y':
        damage = input("What was the damage: ")
        file.write(f"Preexisting Damage: {damage}\n")

    DeviceTestIssues = input("Were there any issues while testing the device Y/N: ")
    if DeviceTestIssues.lower() == 'y':
        test_issues = input("What were the issues while testing: ")
        file.write(f"Issues while testing: {test_issues}\n")

    DeviceTestFailure = input("Were there any failures noticed when testing the device Y/N: ")
    if DeviceTestFailure.lower() == 'y':
        failures = input("What failures were noticed: ")
        file.write(f"Failures noticed: {failures}\n")

    # device info
    DeviceBrand = input("Device Brand: ")
    DeviceModel = input("Device Model: ")
    DeviceColor = input("Color of device: ")
    DeviceAge = input("How old is the device: ")
    file.write(f"Device Brand: {DeviceBrand}\n")
    file.write(f"Device Model: {DeviceModel}\n")
    file.write(f"Device Color: {DeviceColor}\n")
    file.write(f"Device Age: {DeviceAge}\n")

    DeviceIDNumber = input("Do you have the device ID or S/N number Y/N: ")
    if DeviceIDNumber.lower() == 'y':
        id_number = input("Input device ID or S/N number: ")
        file.write(f"Device ID/SN: {id_number}\n")
    else:
        id_reason = input("State reason why: ")
        file.write(f"Reason for no ID/SN: {id_reason}\n")

    DevicePassword = input("Do you have the password for the device Y/N: ")
    if DevicePassword.lower() == 'y':
        password = input("Input password for the device: ")
        file.write(f"Device Password: {password}\n")
    else:
        password_reason = input("State reason why: ")
        file.write(f"Reason for no password: {password_reason}\n")

    Depot = input("Will the device be sent to the depot Y/N: ")
    if Depot.lower() == 'n':
        store_location = input("Where will the device be held in Store: ")
        file.write(f"Device Storage Location: {store_location}\n")

    AdditionalInfo = input("Note any additional Information here: ")
    file.write(f"Additional Information: {AdditionalInfo}\n")

print("Information has been saved to customer_device_info.txt")
