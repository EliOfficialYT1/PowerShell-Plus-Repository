import os
import time

os.system('cls')

Version = '1.0.0'
BuildNumber = 'Sys12MPB5'

SetupSays = 'Downloading Files'
os.system('Color A')

def WindowsCustom7Shell():
    while True:
        UserPowershell7Input = input('AdministratorSystem32:>> ')

        if UserPowershell7Input == 'GetPnp - Clear':
            os.system('cls')
        if UserPowershell7Input == 'GetPnp - Version':
            print(),print(f"System Version: {Version}"),print(f'System Number: {BuildNumber}'),print()

        elif UserPowershell7Input == 'GetPnp - Help?':
            print(),print('>> Custom?Shell Commands. <<'),print(),print("GetPnp - Clear > Wipes the Screen"),print("GetPnp - Version > Show's System Info!"),print()

for SetupShell in range(50):
    if SetupShell >= 45:
        SetupSays = 'Configuring Info'

    print(f'{SetupSays} > Powershell Plus: ', end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: .', end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: ..',end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: ...',end='\r'), time.sleep(0.2)

    os.system('cls')
os.system('cls'), time.sleep(0.75), WindowsCustom7Shell()