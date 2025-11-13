from pathlib import Path
import json, csv
class Repositorio:          
    def __init__(self):                                                                                         #RETORNA UMA PASTA DATA COM AS INFORMAÇÕES DO USUÁRIO
        self.DATA_DIR = Path(__file__).resolve().parent/"data"
        self.DATA_DIR.mkdir(exist_ok=True) 
        self.DB_PATH = self.DATA_DIR/"candidato.json" 

    def _load(self):                                                                                            #CARREGA OS DADOS
            if not self.DB_PATH.exists():
                return[]
            try:
                return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return []
            
    def _save(self, candidato):                                                                                 #SALVA OS DADOS NO BANCO DE DADOS
        self.DB_PATH.write_text(json.dumps(candidato, ensure_ascii=False, indent=2), encoding="utf-8")
    
    def criandoCandidato(self, candidato_user):                                                                 #CRIA UM NOVO CANDIDATO AO RODAR O PROGRAMA
        candidatoCriado = self._load() 
        candidatoCriado.append(candidato_user)
        self._save(candidatoCriado)

    def candidats_db(self):                                                                                    
        return self._load()