import random

# pool = [n for n in range(1,42)]
# elegido = random.choice(pool)
# print(f"el primer numero es {elegido}")
# pool.remove(elegido)
# elegido = random.choice(pool)
# print(f"el segundo numero es {elegido}")
# pool.remove(elegido)
# elegido = random.choice(pool)
# print(f"el comodin es {elegido}")
# pool.remove(elegido)
# elegido = random.choice(pool)
# print(f"el segundo numero es {elegido}")
# pool.remove(elegido)
# elegido = random.choice(pool)
# print(f"el segundo numero es {elegido}")
# pool.remove(elegido)
# elegido = random.choice(pool)
# print(f"el segundo numero es {elegido}")

def sacar_numero (posicion):
    global pool
    pool = [n for n in range(1,42)]
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(pool)
    print(f"el {posicion} numero es {elegido}")

sacar_numero("primero")
sacar_numero("segundo")
sacar_numero("tercero")
sacar_numero("cuarto")
sacar_numero("quinto")
sacar_numero("sexto")
sacar_numero("comodin")
