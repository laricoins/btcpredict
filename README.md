# btcpredict
predict btc PK via Pub Address

проект посвящен исследованиям предугадывания приватного ключа BTC зная публичный ключ
подбор по адресам только 34 длины 

(the project is dedicated to research on predicting the private key of BTC knowing the public key )


2 в папке generate генератор адресов BTC
требования
pip  bitcoinaddress 
запуск в https://colab.research.google.com/
2.1 подключить гоогл диск
2.2 загрузить нужный пакет !pip install bitcoinaddress
2.3 перейди в папку %cd drive/MyDrive/btcpredict/generate
2.4 запустить генератор и ждать. попробуй начать с 1000 увеличивай до 10 000 ( примерное время генерации 1 000 000 адресов около 10 часов 
      !python linegenegator.py --f train.txt --c  10

результат
в папке  generate    будет создан файл train.txt с примерно таким содержимым

1HuC8JmaoatJzYtTztHqerC5hWupyDg8EL;5JVq5zSCpm9pjLsrqDFfsuXkeso5fN1P94nKAS48omz3hvueASG
16C7VFkVT3nBCriKbcZ1WmGQSDPG8St1vR;5KMtC3XmrRBtLqwsNVbxC9prcGUjBu1AgsHjAVAs3S4FLh2j1uu
1CxeDMqbBmeNmQm5j5iRqnM8HpWNkQis3t;5JXYhTHF7ppEJw7Xm4sf5i3DyG18beHwemJb7oq494RL9xs1VS4
16PhVyKjevcVQnuHaiu8UB13PE4TWYg98R;5JxCouAW18DpRLT27vk7fy9NgSfz5kL6Xd3Pb8YhH2LzfqcjuV8
1Fn8wKWVqYkR7sERiYFL6neBD1AYcYKzni;5JbbzvQNhyfDf2zavfYm1ahUgSaaMiRbyiSJjoi9WriK5w9Wcuz
1KJMGYFgQBvCVbWWcup4YhczhCDtUP8S6Y;5J4SPqdN3x8qDUM6GbcviWtWu9VWbb1pCDJZnCy8VtB3HUjd7cB
1JXiL6qfj8Y7tH1E8RRC8pWBvcDQGYMQqp;5KcNmhWmpoJWuDYqXFjgGSspnKe4C8JjpBXunpgqVdCg5GntC6K
173MzhHnEyFYJNLUUUYjWXX3jx7buoXDV8;5Jfzgof18EuXeaLhmtM8L71cPdKsRQ19PbKsD3UGiJs8keNYJ3x
1GExHGfS5PWK2Lir56Rvken5BpqNMQWfqL;5KcfPw6LR4vBnCNudCkr5BZYycxkuyd5GhRqu48QYGtSXkdRtMq
12tT7AkGZ8ycGwRfeRBmLppRWThcnmW35H;5K6KuS3F9cMrVzonwYbTT2fPLxEfXegN78JRFV4ihjq7YphMyui

