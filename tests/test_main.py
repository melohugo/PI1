# import pytest
# from source.main import load_flights, main  # Importa a função main
# from source.utils import ask  # Importa a função ask do módulo utils
# from unittest.mock import patch

# def test_load_flights():
#     # Testa se retorna vazio se o arquivo não existe
#     assert load_flights() == []

# def test_main():
#     # Mock para simular a entrada do usuário
#     with patch('builtins.input', side_effect=['1', '2', 'exit']):
#         # Mock para simular a função load_flights
#         with patch('source.main.load_flights', return_value=[{'id_voo': '1', 'descricao': 'Test Flight'}]):
#             # Mock para simular a função show_graph_menu
#             with patch('source.main.show_graph_menu', return_value='exit'):
#                 # Chama a função main
#                 main()
#                 # Aqui você pode adicionar asserções para verificar o comportamento esperado
#                 # Por exemplo, verificar se as funções foram chamadas corretamente
#                 assert True  # Substitua por asserções reais