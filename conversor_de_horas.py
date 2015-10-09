# Exercícios do http://wiki.python.org.br/ExerciciosFuncoes

def converte_hora(hora, minutos):
    if hora < 12:
        turno= 'AM'
    else:
        turno =  'PM'
    conv = {12:12, 13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11, 0:0}
    
    return '%i:%i %s' %(conv[hora], minutos, turno)
    
def conversor():
    while True:
        print('Conversor de horas!\nDigite uma letra para terminar.\n')
        
        try:
            h = int(input('Digite as horas: '))
            m = int(input('Digite os minutos: '))
            print('\n=== %s ===\n' %converte_hora(h, m))
        
        except:
            print('Fim!')
            break
