# создаем числовой словарь с ключами (от1 до 10)
# вид {key: key**2}
d = {}
for i in range(10):
    d[i+1] = (i+1)**2
print(d)
