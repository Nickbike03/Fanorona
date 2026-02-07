
### 1. Obiettivo del Gioco
L'obiettivo è catturare tutte le pedine dell'avversario o impedire all'avversario di muoversi (stallo).

### 2. La Scacchiera e le Pedine
*   **Griglia:** 5 righe x 9 colonne.
*   **Linee:** Le pedine si muovono solo lungo le linee tracciate.
*   **Intersezioni (Nodi):**
    *   **Nodi Forti:** Intersezioni dove passano le diagonali (8 direzioni possibili).
    *   **Nodi Deboli:** Intersezioni senza diagonali (solo 4 direzioni: su, giù, destra, sinistra).
*   **Setup Iniziale:** 22 pedine bianche e 22 nere. Al centro c'è una pedina vuota.

### 3. Tipi di Movimento
Esistono due macro-tipi di mossa. La regola d'oro è: **La cattura è obbligatoria.**

#### A. Mossa Semplice ("Paika")
*   Si sposta una pedina di un passo lungo una linea verso un'intersezione vuota.
*   **Condizione Fondamentale:** La mossa Paika è permessa **SOLO SE** non è possibile effettuare alcuna cattura in quel turno.

#### B. Mossa con Cattura
Se una pedina può mangiare, **deve** farlo. Esistono due modi per catturare:

1.  **Cattura per Avvicinamento (Approach):**
    *   Muovi la tua pedina in una casella vuota adiacente a una pedina avversaria.
    *   La pedina avversaria deve trovarsi sulla linea di movimento, nella direzione verso cui ti stai muovendo.
    *   **Effetto:** Catturi quella pedina avversaria **e tutte quelle consecutive** dello stesso colore che si trovano dietro di essa lungo quella linea.

2.  **Cattura per Allontanamento (Withdrawal):**
    *   Muovi la tua pedina partendo da una casella adiacente a una pedina avversaria, allontanandoti da essa lungo la linea.
    *   **Effetto:** Catturi la pedina avversaria da cui ti sei allontanato **e tutte quelle consecutive** dietro di essa lungo quella linea.

**Nota Importante (Regola della Scelta):**
Se una singola mossa permette *contemporaneamente* un Avvicinamento e un Allontanamento (verso due gruppi diversi di nemici), il giocatore deve **scegliere** quale gruppo catturare. Non può catturarli entrambi con lo stesso spostamento atomico.

### 4. Catture Multiple (Combo)
Se dopo aver effettuato una cattura, la pedina che si è mossa si trova in una posizione da cui può effettuare un'altra cattura (Approach o Withdrawal), **deve** continuare a muoversi e catturare ancora nello stesso turno.

**Vincoli per le Combo:**
1.  **Non ripassare:** La pedina non può tornare su un'intersezione che ha già visitato durante lo stesso turno.
2.  **Cambio di direzione:** Non si può effettuare una cattura nella stessa direzione (vettore) della mossa immediatamente precedente (es: se hai mangiato muovendoti a Nord, la prossima cattura non può essere ancora verso Nord, deve cambiare direzione).
3.  **Obbligo di continuazione:** La catena di catture si ferma solo quando non ci sono più catture legali possibili o si viola la regola del "non ripassare".
