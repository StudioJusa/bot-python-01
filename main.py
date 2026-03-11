# Bibliotecas = Pacote de Código

# Passo 01: Entrar no sistema da empresa
# Passo 02: Fazer login
# Passo 03: Abrir a base de dados
# Passo 04: Cadastrar um produto
# Passo 05: Repetir o passo 04 até acabar a lista de produtos

# pip install pyautogui
import pyautogui
import time
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# pyautogui.click (para clicar)
# pyautogui.write (para escrever)
# pyautogui.press (para pressionar uma tecla)
# pyautogui.hotkey (para pressionar uma combinação de teclas - atalho)

pyautogui.PAUSE = 0.5 # Tempo de espera entre cada comando (em segundos)

# Passo 01: Abrir navegador
pyautogui.press("win")

pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.sleep(2) # Tempo de espera para o navegador abrir (em segundos)

# Passo 01: Selecionar barra de endereço
pyautogui.hotkey("ctrl", "l")
time.sleep(1)


# Passo 01: Escrever link + enter
pyautogui.write(link)
pyautogui.press("enter")

# Tempo de espera para a página carregar (em segundos)
pyautogui.sleep(2)

# Passo 02: Clicar e escrever email
pyautogui.click(x=698, y=394) # Clicar no campo de email
pyautogui.write("pythonimpressionador@gmail.com") # Escrever email

# Passo 02: Clicar e escrever senha
pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo
pyautogui.write("123456") # Escrever senha

# Passo 02: Fazer login
pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo
pyautogui.press("enter") # Pressionar a tecla enter para fazer login

time.sleep(4) # Tempo de espera para a próxima página carregar (em segundos)

# Passo 03: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv") # Abrir a base de dados (arquivo .csv)
print(tabela) # Imprimir a base de dados para verificar se abriu corretamente


# Passo 04: Cadastrar um produto
for linha in tabela.index: # Para cada linha na tabela, faça:
    pyautogui.click(x=692, y=281) # Clicar no campo - Código do Produto

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo) # Escrever o código do produto
    pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca) # Escrever a marca do produto
    pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo) # Escrever o tipo do produto
    pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(str(categoria)) # Escrever a categoria do produto
    pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco) # Escrever o preço do produto
    pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo) # Escrever o custo do produto
    pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo

    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs) # Escrever OBS do produto
    pyautogui.press("tab") # Pressionar a tecla tab para ir para o próximo campo

    pyautogui.press("enter") # Pressionar a tecla enter para cadastrar o produto

    pyautogui.scroll(5000) # Voltar para o início da tela