#!/usr/bin/env bash

INVENTORY_FILE=benchmark/inventory.ini
SSH_USER=azureadmin
SSH_PRIVATE_KEY=id_azure

new_entry() {
    HOSTNAME=$1
    HOSTIP=$2
    echo "$HOSTNAME ansible_ssh_host=$HOSTIP ansible_ssh_user=$SSH_USER ansible_ssh_private_key_file=$SSH_PRIVATE_KEY" >> "$INVENTORY_FILE"
}

pushd infra
TF_OUT=$(terraform output -json)
popd

echo "[benchmark]" > "$INVENTORY_FILE"
new_entry "standard-c2m7" "100.1.1.1"

cp infra/id_azure benchmark/id_azure
