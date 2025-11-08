import os
import time

os.system('cls')

Version = '3.0.0'
BuildNumber = 'Sys13S45'

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
            print(),print('>> Custom?Shell Commands. <<'),print(),print("GetPnp - Clear > Wipes the Screen"),print("GetPnp - Version > Show's System Info!")
            print("GetPnp - EnterColorEditor > Allow's For Color Changes!"), print(), print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'),print(),print("GetPnp - EnterColorEditor - Enchanted > More Advanced Color Options.")
            print("GetPnp - PlusCalc > Enables Powershell Plus's 3.0 Calculator"), print("GetPnp - PythonReads - Enchanted > Allow's For Python To Read Files. You Give It Access To."),print()

        elif UserPowershell7Input == 'GetPnp - PythonReads - Enchanted':
            fileselection = input('Enter a Vaild .txt Warning. Must Be In Scripts Directory: ')

            with open(fileselection, 'r') as stf:
                content = stf.read()

                print(),print(f'Output: {content}'),print()
        
        elif UserPowershell7Input == 'GetPnp - PlusCalc':
            print()
            
            print(eval(input('Calculate Two Numbers: '))), print()

        elif UserPowershell7Input == 'GetPnp - EnterColorEditor - Enchanted':
            print()

            print('=-=-=-=-=-=Colors=-=-=-=-=-=-=-='),print()

            print('Black                 DarkYellow')
            print('DarkBlue              DarkMagenta')
            print('DarkGreen             Cyan')
            print('DarkCyan              Magenta')
            print('DarkRed               DarkYellow')

            print()
            PowershellInput7 = input('System: Choose Powershell Plus Color: ')
            ComfirmPowershellColorChange = input('System: Comfirm Selection: (Y/N): ')

            if ComfirmPowershellColorChange == 'Y':
                os.system(f'powershell -Command "$Host.UI.RawUI.BackgroundColor = \'{PowershellInput7}\'; Clear-Host"')
            else:
                print(), print("System Won't Change System Colors. Unless You Comfirm."), print()

        elif UserPowershell7Input == 'GetPnp - EnterColorEditor':
            print()

            print('=-=-=-=-=TextColors=-=-=-=-='),print()

            print('Black = 0         Gray = 8 ')
            print('Blue = 1          Light Blue = 9')
            print('Green = 2         Light Green = A')
            print('Aqua = 3          Light Aqua = B')
            print('Red = 4           Light Red = C')
            print('Purple = 5        Light Purple = D')
            print('Yellow = 6        Light Yellow = E')
            print('White = 7         Light White = F')
            print()

            ColorAnswerInput = input('System: Enter The Color Numbers: ')
            StorageColorInput = ColorAnswerInput

            os.system(f'Color {StorageColorInput}')
            print()

for SetupShell in range(0):
    if SetupShell >= 0:
        SetupSays = 'Configuring Info'

    print(f'{SetupSays} > Powershell Plus: ', end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: .', end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: ..',end='\r'), time.sleep(0.2)
    print(f'{SetupSays} > Powershell Plus: ...',end='\r'), time.sleep(0.2)

    os.system('cls')
os.system('cls'), time.sleep(0.75), WindowsCustom7Shell()