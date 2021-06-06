## O que estou assistindo?

`Criado em 03/06/2021 `

Bot simples que a cada 15 minutos recebe um fluxo de video, identifica o canal exibido e faz um tweet com screenshot e dados do canal identificado.
Fluxo de video precisa ser proveniente de placa de captura ligada a decodificador ou conversor digital.

### Como executar?

0 - Verifique suporte de GPU a processamento CUDA
`python verifycuda.py`

1 - Instale dependências

`pip install detecto`
`pip3 install labelImg`

2 - Crie um arquivo `secrets.py` baseando-se em `secrets.py.example` com suas chaves de API do twitter

3 - Insira as bases imagens bases em `/img` e execute `labelImg` para categoriza-las por canal

4 - Crie os modelos de identificação usando `python createmodels.py` (Isso pode levar bastante tempo de acordo com sua GPU, 20 templates demoram 5min em GTX 1650 Super)

5 - Rode `main.py`

Imagens ficam armazenadas também em `/results`
