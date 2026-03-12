# Sliplane Configuration

Este arquivo contém informações sobre a configuração para deploy automático no Sliplane.

## Como configurar no Sliplane

1. **Conectar repositório GitHub**
   - Acesse https://sliplane.io
   - Conecte sua conta GitHub
   - Selecione o repositório: `baduba/carapicuibaemdados`

2. **Configuração do Build**
   - Build Method: Dockerfile
   - Dockerfile Path: `./Dockerfile`
   - Build Context: `/`

3. **Configuração de Porta**
   - Port: `8501`
   - Health Check Path: `/_stcore/health`

4. **Variáveis de Ambiente** (opcional)
   - Nenhuma variável de ambiente é necessária para o MVP
   - Para produção, adicionar chaves de API das fontes de dados

5. **Configuração de Deploy Automático**
   - Branch: `main` ou `master`
   - Deploy automático: ✅ Ativado
   - Build on PR: ✅ Ativado (opcional)

## Comandos úteis

### Build local
```bash
docker build -t carapicuiba-dados .
```

### Run local
```bash
docker run -p 8501:8501 carapicuiba-dados
```

### Verificar logs
```bash
docker logs -f carapicuiba-app
```

### Parar container
```bash
docker stop carapicuiba-app
docker rm carapicuiba-app
```

## CI/CD Pipeline

O pipeline de CI/CD no Sliplane é automático:

1. **Commit** → Push para GitHub
2. **Trigger** → Sliplane detecta mudanças
3. **Build** → Constrói imagem Docker
4. **Test** → Health check automático
5. **Deploy** → Publica nova versão
6. **Live** → Aplicação disponível

## Monitoramento

- **Health Check**: Streamlit fornece endpoint `/_stcore/health`
- **Logs**: Disponíveis no dashboard do Sliplane
- **Metrics**: CPU, Memória, Requisições

## Rollback

Em caso de problemas:
1. Acesse o dashboard do Sliplane
2. Selecione o projeto
3. Clique em "Rollback" para versão anterior
