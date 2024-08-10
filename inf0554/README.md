# Projeto Final INF0554

## Arquitetura

A arquitetura do projeto é composta por uma aplicação web que é executada em um conjunto de máquinas virtuais. A aplicação web é acessada por usuários finais por meio de um balanceador de carga. O balanceador de carga distribui o tráfego entre as máquinas virtuais que executam a aplicação web. O conjunto de máquinas virtuais é gerenciado por um conjunto de escalas, que aumenta ou diminui o número de máquinas virtuais com base na carga da CPU.

Um Load Balancer foi criado para distribuir o tráfego entre as máquinas virtuais. O Load Balancer é um serviço que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais. O Load Balancer é um serviço de rede que distribui o tráfego de entrada entre várias máquinas virtuais.

## Criação da Infraestrutura

Para criar a infraestrutura, foi utilizado o Terraform. O Terraform é uma ferramenta de infraestrutura como código (IaC) que permite criar, alterar e versionar a infraestrutura de forma segura e eficiente. O Terraform permite que a infraestrutura seja descrita em um arquivo de configuração que define quais recursos devem ser provisionados e como eles devem ser configurados.

Primeiramente precisamos fazer login na Azure:

```
az login
```

Em seguida, inicializamos o Terraform:

```
terraform init
```

E então, aplicamos o plano:

```
terraform apply
```

## AutoScaling

Para realizar o auto scaling de uma aplicação, é necessário monitorar a utilização de recursos da aplicação e, a partir disso, decidir se é necessário aumentar ou diminuir a quantidade de instâncias da aplicação. Para isso, é necessário definir métricas que serão monitoradas e definir regras para decidir quando aumentar ou diminuir a quantidade de instâncias.

Na Azure, o serviço que realiza o auto scaling é o Azure Monitor. O Azure Monitor é um serviço de monitoramento de nuvem unificado que fornece análises abrangentes em tempo real, retenção de dados de longo prazo e alertas com base em métricas. O Azure Monitor coleta dados de telemetria de uma variedade de fontes e fornece uma experiência unificada para visualização, pesquisa, análise e alerta.

A seguir, será apresentado um exemplo de como realizar o auto scaling de uma aplicação na Azure.

```
rule {
    metric_trigger {
        metric_name     = "Percentage CPU"
            metric_resource_id = azurerm_orchestrated_virtual_machine_scale_set.vmss_terraform_tutorial.id
        operator        = "LessThan"
        statistic       = "Average"
        time_aggregation   = "Average"
        time_window     = "PT2M"
        time_grain      = "PT1M"
        threshold       = 10
    }
    scale_action {
        direction = "Decrease"
        type    = "ChangeCount"
        value   = "1"
        cooldown  = "PT1M"
    }
}
rule {
    metric_trigger {
        metric_name     = "Percentage CPU"
        metric_resource_id = azurerm_orchestrated_virtual_machine_scale_set.vmss_terraform_tutorial.id
        operator        = "GreaterThan"
        statistic       = "Average"
        time_aggregation   = "Average"
        time_window     = "PT2M"
        time_grain      = "PT1M"
        threshold       = 90
}
    scale_action {
        direction = "Increase"
        type    = "ChangeCount"
        value   = "1"
        cooldown  = "PT1M"
    }
}
```

Essas duas regras instruem o conjunto de escalas a adicionar uma VM quando a carga média da CPU for superior a 90% e a remover uma VM quando for inferior a 10%. O parâmetro scale_action em cada regra de autoescala configura o conjunto de escalas para adicionar ou remover apenas uma VM por vez, e o parâmetro cooldown configura o conjunto de escalas para aguardar um minuto entre as ações de escalonamento. Lembre-se de que o perfil de autoescala que você criou na etapa anterior garante um mínimo de 1 e um máximo de 10 máquinas virtuais em execução.
