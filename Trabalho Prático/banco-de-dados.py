#Trabalho prático python I
#Este código é um sistema de gerenciamento de usuários, serviços e agendamentos.
#Utiliza arquivos JSON para armazenar os dados e oferece operações de CRUD (Create, Read, Update, Delete).
#Estruturas de dados
import json

#Nomes dos arquivos JSON que armazenam os dados
arquivo_usuarios = "dados-usuario.json"
arquivo_serviços = "dados-serviço.json"
arquivo_agendamentos = "dados-agendamentos.json"

#Variável para rastrear alterações nos dados
dados_alterados = False

#Carregar dados de um arquivo JSON
def carregar_dados(arquivo):   
    #Abre o arquivo no modo leitura   
    try:
        with open(arquivo, "r") as file:
            dados = json.load(file)

            if arquivo == arquivo_usuarios:
                dados = [usuario for usuario in dados if "nome" in usuario and "nivel" in usuario and "senha" in usuario]
            elif arquivo == arquivo_serviços:
                dados = [servico for servico in dados if "nome" in servico and "preço" in servico]
            elif arquivo == arquivo_agendamentos:
                dados = [agendamento for agendamento in dados if "cliente" in agendamento and "serviço" in agendamento and "data" in agendamento and "hora" in agendamento]

            return dados
    except FileNotFoundError:
        #Retorna uma lista vazia se o arquivo não existir
        return []

#Salvar dados nos arquivos JSON
def salvar_dados(arquivo, dados):
    print(f"Salvando dados no arquivo {arquivo}...")
    with open(arquivo, "w") as file:
        #Salva os dados com formatação
        json.dump(dados, file, indent=4)




#CRUD
#CRUD usuários
#Create
def criar_usuario(usuarios):
    global dados_alterados
    nome = input("Nome: ").strip()
    nivel = input("Nível de acesso (dono, cliente): ").lower().strip()
    #Valida o nível de acesso
    while nivel not in ["dono", "cliente"]:
        print("Nível de acesso inválido. Digite 'dono' ou 'cliente'.")
        nivel = input("Nível de acesso (dono, cliente): ").lower().strip()
    senha = input("senha: ")
    novo_usuario = {"nome": nome, "nivel": nivel, "senha": senha}
    #Adiciona o novo usuário à lista
    usuarios.append(novo_usuario)
    #Marca que os dados foram alterados
    dados_alterados = True 
    print("Usuário cadastrado com sucesso!")

#Read
def listar_usuarios(usuarios):
    print("\nLista de Usuários")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, nivel: {usuario['nivel']}")

#Update
def atualizar_usuario(usuarios):
    global dados_alterados
    nome = input("Digite o nome do usuário a ser atualizado: ")
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print("Deixe o campo do que não quiser alterar vazio.")
            novo_nome = input(f"Novo nome ({usuario['nome']}): ").strip() or usuario['nome']
            novo_nivel = input(f"Novo nível ({usuario['nivel']}): ").strip() or usuario['nivel']
            nova_senha = input(f"Nova senha: ") or usuario['senha']
            #Atualiza os dados do usuário
            usuario.update({"nome": novo_nome, "nivel": novo_nivel, "senha": nova_senha})
            dados_alterados = True 
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado.")

#Delete
def deletar_usuario(usuarios):
    global dados_alterados
    nome = input("Digite o nome do usuário a ser deletado: ").strip()
    for usuario in usuarios:
        if usuario['nome'] == nome:
            #Remove o usuário da lista
            usuarios.remove(usuario)
            dados_alterados = True 
            print("Usuário deletado com sucesso!")
            return
    print("Usuário não encontrado.")


#CRUD serviços
#Create
def criar_serviços(servicos):
    global dados_alterados
    nome = input("Nome do serviço: ")
    preço = float(input("Preço: "))
    novo_serviço = {"nome": nome, "preço": preço}
    servicos.append(novo_serviço)
    dados_alterados = True 
    print("Serviço cadastrado com sucesso!")

#Read
#Ordena por nome e preço
def listar_servicos(servicos, ordenar_por=None):
    if ordenar_por == "nome":
        servicos.sort(key=lambda x: x.get("nome", ""))
    elif ordenar_por == "preço":
        servicos.sort(key=lambda x: x.get("preço", 0))

    print("\nLista de serviços:")
    for servico in servicos:
        nome = servico.get("nome", "Desconhecido")
        preço = servico.get("preço", 0.0)
        print(f"Nome: {nome}, Preço: {preço:.2f}")
        
def buscar_servico(servicos):
    nome = input("Digite o nome do produto que deseja buscar: ")
    for servico in servicos:
        if servico['nome'].lower() == nome.lower():
            print(f"Serviço encontrado: Nome: {servico['nome']}, Preço: ${servico['preço']}")
            return
    print("Serviço não encontrado.")

#Update
def atualizar_servico(servicos):
    global dados_alterados
    nome = input("Digite o nome do serviço a ser atualizado: ")
    for servico in servicos:
        if servico['nome'] == nome:
            print("Deixe o campo do que não quiser alterar vazio.")
            novo_nome = input(f"Novo nome ({servico['nome']}): ") or servico['nome']
            novo_preço = input(f"Novo preço ({servico['preço']}): ")

            if novo_preço:
                try:
                    novo_preço = float(novo_preço) #Converte o preço para float
                except ValueError:
                    print("Preço inválido. O preço não foi alterado.")
                    novo_preço = servico['preço']
            else:
                novo_preço = servico['preço']
            dados_alterados = True 
            servico.update({
               "nome": novo_nome, 
               "preço": novo_preço
               })
            print("Serviço atualizado com sucesso!")
            return
    print("Serviço não encontrado.")

#Delete
def deletar_servicos(servicos):
    global dados_alterados
    nome = input("Digite o nome do serviço a ser deletado: ")
    for servico in servicos:
        if servico['nome'] == nome:
            servicos.remove(servico)
            dados_alterados = True 
            print("Serviço deletado com sucesso!")
            return
    print("Serviço não encontrado.")


#Agendamentos
#Create
def agendar_servico(usuarios, serviços, agendamentos):
    global dados_alterados
    nome = input("Digite seu nome para confirmar: ").strip()
    #Verificar se é cliente ou dono
    usuario_encontrado = next((usuario for usuario in usuarios if usuario["nome"] == nome), None)
    if not usuario_encontrado:
        print("Usuário não encontrado! Somente clientes cadastrados ou donos podem agendar serviços.")
        return
    
    nivel_usuario = usuario_encontrado["nivel"]
    #Se for dono, pode escolher o cliente
    if nivel_usuario == "dono":
        cliente_nome = input("Digite o nome do cliente para quem deseja agendar: ").strip()
        cliente_encontrado = next((usuario for usuario in usuarios if usuario["nome"] == cliente_nome and usuario["nivel"] == "cliente"), None)
        if not cliente_encontrado:
            print("Cliente não encontrado!")
            return
    else:
        #Cliente só pode agendar para si mesmo
        cliente_nome = nome  

    listar_servicos(serviços)
    nome_servico = input("Digite o nome do serviço que deseja agendar: ").strip()
    servico_encontrado = next((i for i in serviços if i["nome"].lower() == nome_servico.lower()), None)
    if not servico_encontrado:
        print("Serviço não encontrado!")
        return

    data = input("Digite a data do agendamento (DD-MM-AAAA): ")
    hora = input("Digite a hora do agendamento (HH:MM): ")

    novo_agendamento = {
        "cliente": cliente_nome,
        "serviço": nome_servico,
        "data": data,
        "hora": hora,
    }

    agendamentos.append(novo_agendamento)
    salvar_dados(arquivo_agendamentos, agendamentos)
    dados_alterados = True
    print("Agendamento realizado com sucesso!")


#Read
def listar_agendamentos(agendamentos, usuario):
    print(f"Usuário logado: {usuario}")
    print("\nLista de Agendamentos:")
    if usuario["nivel"] == "dono":
        # Dono pode ver todos os agendamentos
        for agendamento in agendamentos:
            print(f"Cliente: {agendamento['cliente']}, Serviço: {agendamento['serviço']}, Data: {agendamento['data']}, Hora: {agendamento['hora']}")
    else:
        # Cliente só pode ver seus próprios agendamentos
        agendamentos_cliente = [a for a in agendamentos if a["cliente"] == usuario["nome"]]
        if not agendamentos_cliente:
            print("Você ainda não tem nenhum agendamento.")
        else:
            for agendamento in agendamentos_cliente:
                print(f"Serviço: {agendamento['serviço']}, Data: {agendamento['data']}, Hora: {agendamento['hora']}")


#Update
def atualizar_agendamento(agendamentos):
    global dados_alterados
    nome_cliente = input("Digite o nome do cliente que pertence o agendamento a ser atualizado: ").strip()
    for agendamento in agendamentos:
        if agendamento['cliente'] == nome_cliente:
            print("Deixe o campo do que não quiser alterar vazio.")
            novo_nome = input(f"Novo nome ({agendamento['cliente']}): ").strip() or agendamento['cliente']
            novo_serviço = input(f"Novo serviço ({agendamento['serviço']}): ").strip() or agendamento['serviço']
            nova_data = input(f"Nova data: ") or agendamento['data']
            nova_hora = input(f"Novo horário: ") or agendamento['hora']
            agendamento.update({"cliente": novo_nome, "serviço": novo_serviço, "data": nova_data, "hora": nova_hora})
            dados_alterados = True 
            print("Agendamento atualizado com sucesso!")
            return
    print("Agendamento não encontrado.")

#Delete
def deletar_agendamento(agendamentos):
    global dados_alterados
    nome = input("Digite o nome do cliente que pertence o agendamento a ser atualizado: ").strip()
    for agendamento in agendamentos:
        if agendamento['cliente'] == nome:
            agendamentos.remove(agendamento)
            dados_alterados = True 
            print("Agendamento deletado com sucesso!")
            return
    print("Agendamento não encontrado.")




#Menus
#Menu dono
def menu_dono(usuarios, servicos, agendamentos, usuario_logado):
    global dados_alterados
    while True:
        print("\nMenu Dono:")
        print("1. Gerenciar usuários")
        print("2. Gerenciar serviços")
        print("3. Gerenciar agendamentos")
        print("4. Salvar e sair")
        print("5. Sair sem salvar")
        opcao = input("Escolha uma opção(1-5): ")
        if opcao == "1":
            menu_crud_usuarios(usuarios)
        elif opcao == "2":
            menu_crud_servicos(servicos)
        elif opcao == "3":
            menu_crud_agendamentos(usuarios, servicos, agendamentos, usuario_logado)
        elif opcao == "4":
            salvar_dados(arquivo_usuarios,usuarios)
            salvar_dados(arquivo_serviços, servicos)
            dados_alterados = False
            print("Dados salvos com sucesso. Saindo...")
            break
        elif opcao == "5":
            if dados_alterados:
                confirmacao = input("Há alterações não salvas. Deseja realmente sair sem salvar? (sim/não): ").lower()
                if confirmacao == "sim":
                    print("Saindo sem salvar...")
                    break
            else:
                print("Saindo sem salvar")
                break
        else:
            print("Opção inválida!")


#Menu cliente
def menu_cliente(usuarios, serviços, agendamentos, usuario_logado):
    while True:
        print("\nMenu Cliente:")
        print("1. Ver opções de serviços")
        print("2. Agendar serviços")
        print("3. Ver meus agendamentos")
        print("4. Salvar e sair")
        print("5. Sair sem salvar")
        opcao = input("Escolha uma opção(1-5): ")
        if opcao == "1":
            listar_servicos(serviços)
        elif opcao == "2":
            agendar_servico(usuarios, serviços,agendamentos)
        elif opcao == "3":
            listar_agendamentos(agendamentos, usuario_logado)
        elif opcao == "4":
            salvar_dados(arquivo_usuarios,usuarios)
            salvar_dados(arquivo_serviços, serviços)
            salvar_dados(arquivo_agendamentos, agendamentos)
            dados_alterados = False
            print("Dados salvos com sucesso. Saindo...")
            break
        elif opcao == "5":
            if dados_alterados:
                confirmacao = input("Há alterações não salvas. Deseja realmente sair sem salvar? (sim/não): ").lower()
                if confirmacao == "sim":
                    print("Saindo sem salvar...")
                    break
            else:
                print("Saindo sem salvar")
                break
        else:
            print("Opção inválida!")


#Menus de interações com usuários
def menu_crud_usuarios(usuarios):
    while True:
        print("\nGerenciamento de Usuários:")
        print("1. Cadastrar usuário")
        print("2. Listar usuário")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Voltar (Para salvar volte para o menu e selecione 4)")
        opcao = input("Escolha a opção(1-5): ")
        if opcao == "1":
            criar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            atualizar_usuario(usuarios)
        elif opcao == "4":
            deletar_usuario(usuarios)
        elif opcao == "5":
            break
        else:
            print("Opção invalida!")

def menu_crud_servicos(servicos):
    while True:
        print("\nGerenciamento de serviços:")
        print("1. Cadastrar serviço")
        print("2. Listar serviço")
        print("3. Atualizar serviço")
        print("4. Deletar serviço")
        print("5. Voltar (Para salvar volte para o menu e selecione 4)")
        opcao = input("Escolha a opção: ")
        if opcao == "1":
            criar_serviços(servicos)
        elif opcao == "2":
            listar_servicos(servicos)
        elif opcao == "3":
            atualizar_servico(servicos)
        elif opcao == "4":
            deletar_servicos(servicos)
        elif opcao == "5":
            break
        else:
            print("Opção invalida!")

def menu_crud_agendamentos(usuarios, serviços, agendamentos, usuario_logado):
    while True:
        print("\nGerenciamento de agendamentos:")
        print("1. Cadastrar agendamento")
        print("2. Listar agendamento")
        print("3. Atualizar agendamento")
        print("4. Deletar agendamento")
        print("5. Voltar (Para salvar volte para o menu e selecione 4)")
        opcao = input("Escolha a opção: ")
        if opcao == "1":
            agendar_servico(usuarios, serviços, agendamentos)
        elif opcao == "2":
            listar_agendamentos(agendamentos, usuario_logado)
        elif opcao == "3":
           atualizar_agendamento(agendamentos)
        elif opcao == "4":
           deletar_agendamento(agendamentos)
        elif opcao == "5":
            break
        else:
            print("Opção invalida!")




#Execução principal do programa
def main():
    usuarios = carregar_dados(arquivo_usuarios)
    servicos = carregar_dados(arquivo_serviços)
    agendamentos = carregar_dados(arquivo_agendamentos)

    print("Bem vindo ao Sistema de gerenciamento!")
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    usuario_encontrado = next((u for u in usuarios if u['nome'] == usuario and u['senha'] == senha), None)
    if usuario_encontrado:
        if usuario_encontrado['nivel'] == "dono":
            menu_dono(usuarios, servicos, agendamentos, usuario_encontrado)
        elif usuario_encontrado['nivel'] == "cliente":
            menu_cliente(usuarios, servicos, agendamentos, usuario_encontrado)
        else:
            print("Permissão negada!")
            salvar_dados(arquivo_usuarios, usuarios)
            salvar_dados(arquivo_serviços, servicos)
            salvar_dados(arquivo_agendamentos, agendamentos)
            return
    else:
        print("Usuário ou senha incorretos!")

if __name__ == "__main__":
    main()
