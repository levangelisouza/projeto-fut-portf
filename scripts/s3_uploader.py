# -*- coding: utf-8 -*-
import boto3

# Configurações
bucket_name = 'projeto-fut-portf'
base_path = 'dados-raw/'

arquivos = [
    'appearances.csv',
    'club_games.csv',
    'clubs.csv',
    'competitions.csv',
    'game_events.csv',
    'game_lineups.csv',
    'games.csv',
    'players.csv',
    'player_valuations.csv',
    'transfers.csv'
]

# Cliente S3
s3 = boto3.client('s3')

# Movimentação de arquivos
for arquivo in arquivos:
    nome = arquivo.replace('.csv', '')
    origem = f'{base_path}{arquivo}'
    destino = f'{base_path}{nome}/{arquivo}'

    print(f'Movendo: {origem} → {destino}')
    
    # Copiar arquivo para subpasta
    s3.copy_object(
        Bucket=bucket_name,
        CopySource=f'{bucket_name}/{origem}',
        Key=destino
    )

    # Remover arquivo original
    s3.delete_object(Bucket=bucket_name, Key=origem)

print("Arquivos organizados em subpastas com sucesso.")
