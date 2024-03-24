#!/usr/bin/env bash

ROOTDIR=$(dirname $0)
OUTDIR="$ROOTDIR/data"

get_bits() {
    xxd -b "$1" | cut -d ' ' -f 2-7 | tr -d ' ' | tr -d '\n'
}

echo "Preparando diretório data..."
[ -d "$OUTDIR" ] && rm -r "$OUTDIR"; mkdir -p "$OUTDIR"
pushd "$OUTDIR"

echo "Gerando mensagens..."
for N in {1..10}; do 
    openssl rand --hex 16 | head --bytes=16 > "M$N"
    cp "M$N" "M$N'"
done

echo "Gerando chave..."
openssl rand --hex 16 > K

echo "---------------------------------------------------------------------"
echo "Edite manualmente 1 byte nas mensagens M1', M2'... M10'."
read -p "Os arquivos M1', M2'... M10' foram editados? (Enter para continuar) "

echo "Cifrando mensagens..."
CYPHER_KEY=$(cat K)
for N in {1..10}; do
    # Após editar as msgs pode ser que um caracter \n seja inserido nos arquivos.
    # Devemos garantir os 16 bytes da mensagem removendo o \n final.
    cat "M$N'" | head --bytes=16 > "M$N'.tmp"
    mv "M$N'.tmp" "M$N'" 

    cat "M$N" | openssl enc -aes-128-ecb -K "$CYPHER_KEY" -nopad > "C$N"
    cat "M$N'" | openssl enc -aes-128-ecb -K "$CYPHER_KEY" -nopad > "C$N'"
done

echo "Calculando taxa de bits diferentes..."
for N in {1..10}; do
    BITS=$(get_bits "C$N")
    BITSL=$(get_bits "C$N'")
    RATE=$("../calc-bits.py" "$BITS" "$BITSL")
    echo "Mensagem: M$N, taxa de bits diferentes: $RATE"
done
