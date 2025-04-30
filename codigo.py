import win32api
import win32con
import pywintypes

def listar_resolucoes_suportadas():
    modos = []
    i = 0
    while True:
        try:
            modo = win32api.EnumDisplaySettings(None, i)
            resolucao = (modo.PelsWidth, modo.PelsHeight)
            if resolucao not in modos:
                modos.append(resolucao)
            i += 1
        except:
            break
    return modos

def alterar_resolucao(largura, altura):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = largura
    devmode.PelsHeight = altura
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    resultado = win32api.ChangeDisplaySettings(devmode, 0)

    if resultado == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f'Resolução alterada para {largura}x{altura}')
    elif resultado == win32con.DISP_CHANGE_RESTART:
        print('Alteração exige reinício do sistema.')
    else:
        print(f'Erro ao alterar resolução. Código de erro: {resultado}')

def main():
    print('Resoluções suportadas:')
    resolucoes = listar_resolucoes_suportadas()
    for i, (w, h) in enumerate(resolucoes):
        print(f'{i+1}. {w}x{h}')

    escolha = int(input('\nDigite o número da resolução desejada: ')) - 1
    if 0 <= escolha < len(resolucoes):
        largura, altura = resolucoes[escolha]
        alterar_resolucao(largura, altura)
    else:
        print('Escolha inválida.')

if __name__ == '__main__':
    main()
