# README.md

## Monitoraggio dello Stato di un PC Remoto

Questo script Python consente di monitorare lo stato di un secondo PC (remoto) verificando periodicamente se è raggiungibile tramite il protocollo ICMP (ping). Quando il PC remoto risulta online, il programma invia una notifica desktop e termina l'esecuzione.

### Requisiti
Per utilizzare questo script, è necessario avere:
- **Python 3.x** installato sul sistema.
- I seguenti pacchetti Python:
  - [`ping3`](https://pypi.org/project/ping3/): per effettuare il ping al PC remoto.
  - [`plyer`](https://pypi.org/project/plyer/): per inviare notifiche desktop.

Puoi installarli con il comando:
```bash
pip install ping3 plyer
```

### Funzionamento

1. **Input dell'indirizzo IP:**
   - L'utente fornisce l'indirizzo IP del PC remoto da monitorare.
   - Se l'indirizzo IP non viene fornito, il programma restituisce un errore.

2. **Monitoraggio:**
   - Lo script utilizza il modulo `ping3` per inviare richieste ICMP all'indirizzo IP specificato.
   - Se il PC risponde al ping, significa che è online e lo script invia una notifica desktop.
   - Se il PC non è online, il programma attende 5 secondi prima di riprovare.

3. **Notifica Desktop:**
   - Quando il PC remoto diventa raggiungibile, il modulo `plyer` genera una notifica desktop con il messaggio: `"The PC is online."`.
   - Dopo aver inviato la notifica, il programma termina.


### Come eseguire lo script
1. Salva il codice in un file, ad esempio `script.py`.
2. Esegui lo script tramite terminale o IDE Python:
   ```bash
   python script.py
   ```
3. Inserisci l'indirizzo IP del PC remoto quando richiesto.

### Nota
- Assicurati che il PC remoto risponda alle richieste ICMP (ping). Potrebbe essere necessario configurare il firewall sul PC remoto per consentire il ping.
- Il programma si interrompe automaticamente quando il PC remoto diventa raggiungibile.
