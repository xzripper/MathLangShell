from os.path import exists
from os import system, chdir

core = input('Core ("D:\\MathLang\\mathlang.cmd): ')

print(f'DEBUG: DONE, CORE: {core}')

print('DEBUG: VERIFYING CORE')

if not exists(core):
    print('FATAL: CORE NOT EXISTS')
    exit(1)

elif not core.endswith('.cmd'):
    print('FATAL: NOT .CMD')
    exit(1)

elif not exists(core) and not core.endswith('.cmd'):
    print('FATAL: CORE NOT EXISTS, AND ITS NOT A .CMD')
    exit(1)

elif exists(core) and core.endswith('.cmd'):
    print('DEBUG: VERIFIED, CORE IS VALID')
    print('DEBUG: INITING SHELL')
    print('DEBUG: REGISTERING DATA')

    activity = True

    print('DEBUG: REGISTERED')

    print('DEBUG: STARTING')

    print('DEBUG: CHANGING DIR')

    chdir(('\\'.join(core.split('\\')[:-1]) + '\\'))

    print('DEBUG: DIR CHANGED')    

    while activity:
        try:
            line = input('~ ')

            if line.startswith('!get'):
                file = ('\\'.join(__file__.split('\\')[:-1]) + '\\') + 'Lines.mtl'
                method = line.split(' ')[1]

                system(f'{core} {file} {method}')

            elif line == '!vrs':
                system(f'{core} --version')

            elif line == '!cl':
                with open((('\\'.join(__file__.split('\\')[:-1]) + '\\') + 'Lines.mtl'), 'w') as linesfile:
                    linesfile.write('')

            elif line == '!ex':
                activity = not True

            else:
                with open((('\\'.join(__file__.split('\\')[:-1]) + '\\') + 'Lines.mtl'), 'a') as linesfile:
                    linesfile.write(f'{line}\n')
        except Exception as err:
            print(f'FATAL: AN EXCEPTION OCCURED, MSG: {str(err)}')

    print('DEBUG: DONE')
    print('DEBUG: ABANDONING')

    exit(0)
