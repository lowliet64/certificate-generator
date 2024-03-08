from cx_Freeze import setup, Executable

setup(name='Gerador de certificados',
      version='0.1',
      description='Gera certificados automatizados com base num arquivo base',
      executables=[Executable('main.py')])