# Implementazione AI ASP per Fanorona

## Obiettivo
Implementare una modalità "Player vs ASP AI" utilizzando il solver DLV.

## Componenti

### 1. `fanorona.dl` (ASP)
- **Input**: `cell(Row, Col, Color).`
- **Output**: `do_move(FX, FY, TX, TY, Type).`
- **Logica**:
    - Definizione griglia 5x9.
    - Adiacenze (ortogonali e diagonali "strong" vs "weak").
    - Regole di cattura (Approach/Withdrawal).
    - Hard Constraint: Mossa valida.
    - Weak Constraint: Massimizzare catture.

### 2. `asp_agent.py` (Python)
- Ponte tra `Fanorona.py` e `dlv`.
- Classe `ASPAgent`:
    - `get_best_move(board_state, turn_color)`:
        1.  Scrive `facts.dl` in `.tmp/`.
        2.  Chiama `dlv.exe fanorona.dl .tmp/facts.dl`.
        3.  Legge l'output.
        4.  Restituisce la mossa.

### 3. `Fanorona.py` (Integration)
- Aggiunta opzione menu.
- Integrazione loop di gioco.

## Dettagli Tecnici
- **Pedine**: 1=Nero, 2=Bianco.
- **Griglia**: 0..8 (X), 0..4 (Y).
- **Adiacenze**:
    - "Strong" (nodi intersecati dalle diagonali): permettono movimento in 8 direzioni.
    - "Weak": permettono movimento solo a croce (4 direzioni).
    - Pattern a scacchiera per le intersezioni.
