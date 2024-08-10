terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.51.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "3.5.1"
    }

    azapi = {
      source = "Azure/azapi"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
}

data "azurerm_client_config" "current" {}

# A resource group is like a folder for related resources. You can delete the resource group to delete all resources in it.
resource "azurerm_resource_group" "rg" {
  name     = "project-inf0554"
  location = "eastus"
}
