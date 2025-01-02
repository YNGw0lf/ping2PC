## Come funziona:

1.  check_pc_online invia un ping all'indirizzo IP del secondo PC. Se il ping ha successo, significa che il secondo PC è online.
2.  Se il secondo PC è online, lo script invia una notifica tramite la libreria plyer.
3.  Lo script si ripete ogni 5 secondi (puoi modificare il tempo di attesa se necessario).
4.  Una volta che il secondo PC viene rilevato come acceso, il ciclo si interrompe e la notifica viene inviata.

## Avvio automatico dello script

Per far partire automaticamente questo script ogni volta che accendi il primo PC, puoi:

Windows: Aggiungere lo script alle Task Scheduler (Operazioni pianificate) in Windows.
Linux: Utilizzare cron per eseguire lo script all'avvio del sistema.

## Aggiungere lo script all'avvio su Windows:

1.  Cerca e apri Task Scheduler.
2.  Crea una nuova attività.
3.  Nella scheda Trigger, imposta l'azione su "All'avvio".
4.  Nella scheda Action, imposta l'azione su "Avvia programma" e seleziona lo script Python da eseguire.

## Aggiungere lo script all'avvio su Linux:

Aggiungi lo script a cron per eseguirlo all'avvio:
crontab -e
Aggiungi la seguente riga per eseguire lo script all'avvio:
@reboot python3 /percorso/del/tuo/script.py

<h1>ENG explanation</h1>

## How it works:

1.  check_pc_online sends a ping to the second PC's IP address. If the ping is successful, it means the second PC is online.
2.  If the second PC is online, the script sends a notification via the plyer library.
3.  The script repeats every 5 seconds (you can modify the waiting time if necessary).
4.  Once the second PC is detected as being online, the loop stops, and the notification is sent.

## Automatic script startup

To run this script automatically every time you turn on your first PC, you can:

Windows: Add the script to Task Scheduler.
Linux: Use cron to run the script at system startup.

## Adding the script to startup on Windows:

1.  Open and search for Task Scheduler.
2.  Create a new task.
3.  In the Trigger tab, set the action to "At startup".
4.  In the Action tab, set the action to "Start a program" and select the Python script to execute.

## Adding the script to startup on Linux:

Add the script to cron to run it at startup:
crontab -e
Add the following line to run the script at startup:
@reboot python3 /path/to/your/script.py