import time
import asyncio as a
import multiprocessing as mp


print(mp.cpu_count(), "cores", mp.cpu_count() * 2, "threads", mp.process.current_process())


async def calcular_imposto(faturamento):
    imposto = faturamento * 0.03
    print(f"O imposto a ser pago é de: {imposto}")
    return imposto


async def calcular_bonus_funcionario(vendas=dict):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(f"Funcionário:{funcionario}, Bonus: {venda * 0.15}")
        await a.sleep(1)


async def fechamento():
    vendas = {
        "lira": 15000,
        "marcos": 20000,
        "joao": 5000,
    }

    faturamento = 5000
    # tarefa1 = a.create_task(calcular_bonus_funcionario(vendas))
    # tarefa2 = a.create_task(calcular_imposto(faturamento))
    # imposto = await tarefa2
    # await tarefa1

    data = await a.gather(calcular_bonus_funcionario(vendas), calcular_imposto(faturamento))
    _ = data[0]
    imposto = data[1]

    print(f"O imposto a ser pago é de: {imposto}")
    print(f"O faturamento da empresa é de: {faturamento}")


a.run(fechamento())
