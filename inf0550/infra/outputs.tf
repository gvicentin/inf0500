output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "key_data" {
  value = azapi_resource_action.ssh_public_key_gen.output.publicKey
}

output "hostnames" {
  value = azurerm_linux_virtual_machine.terraform_vms[*].name
}

output "public_ip_addresses" {
  value = azurerm_linux_virtual_machine.terraform_vms[*].public_ip_address
}
