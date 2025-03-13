from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reds')

layout = [
    [sg.Text('Pomodoro Timer', font=('Impact', 70),
             justification='center', expand_x=True)],
    [sg.Slider(range=(30, 480), default_value=60, orientation='h',
               size=(15, 20), font=('Impact', 30), key='work', expand_x=True)],
               
    [sg.Button('Iniciar', font=('Impact', 30), expand_x=True)],
    [sg.Button('Parar', font=('Impact', 30), expand_x=True)],
    [sg.Button('Sair', font=('Impact', 30), expand_x=True)],
    [sg.Text('0:00:00', font=('Impact', 120), justification='center',
             expand_x=True, key='timer')],
    [sg.Text('Rest Time 00:00', font=('Impact', 30), justification='center',
             expand_x=True, key='rest')],
]

janela = sg.Window('Pomodoro Timer', layout, size=(1280, 880))

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Iniciar':
        work_time = int(valores['work']) * 60
        while work_time >= 0:
            eventos, valores = janela.read(timeout=1000)
            if eventos == 'Parar' or eventos == sg.WINDOW_CLOSED:
                work_time = 0
                rest_time = 0
                break
            minutos, segundos = divmod(work_time, 60)
            janela['timer'].update(f'{minutos:02d}:{segundos:02d}')
            eventos, valores = janela.read(timeout=1000)

            if eventos == 'Parar' or eventos == 'Sair' or eventos == sg.WINDOW_CLOSED:
                work_time = 0
                rest_time = 0
                break

            minutos, segundos = divmod(work_time, 60)
            janela['timer'].update(f'{minutos:02d}:{segundos:02d}')
            work_time -= 1
            if work_time % (25 * 60) == 0 and work_time != 0:
                rest_time = 5 * 60
                while rest_time >= 0:
                    eventos, valores = janela.read(timeout=1000)
                    if eventos == 'Parar' or eventos == sg.WINDOW_CLOSED:
                        work_time = 0
                        rest_time = 0
                        break
                    rest_minutos, rest_segundos = divmod(rest_time, 60)
                    janela['rest'].update(f'Rest Time {rest_minutos:02d}:{rest_segundos:02d}')
                    rest_time -= 1
                    
    if eventos == 'Parar':
        work_time = 0
        rest_time = 0
        janela['timer'].update('0:00:00')
        janela['rest'].update('Rest Time 00:00')
        
    if eventos == 'Sair':
        break

