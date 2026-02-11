import subprocess
import os
import re

class ASPAgent:
    def __init__(self, dlv_path="dlv.exe", rules_path="fanorona.txt", work_dir=".tmp"):
        # Use absolute path for dlv.exe if it's just a filename
        if not os.path.isabs(dlv_path):
            self.dlv_path = os.path.abspath(dlv_path)
        else:
            self.dlv_path = dlv_path
            
        self.rules_path = rules_path
        self.work_dir = work_dir
        
        # Ensure work directory exists
        if not os.path.exists(self.work_dir):
            os.makedirs(self.work_dir)

    def get_best_move(self, pieces, turn_color_code):
        """
        Calculates the best move using ASP.
        pieces: 5x9 list of lists (0=Empty, 1=Black, 2=White)
        turn_color_code: 1 for Black, 2 for White (matches pieces values)
        Returns: (FromX, FromY, ToX, ToY, CaptureType) or None
        """
        print("\n[ASP AI] Inizio ciclo decisionale.")
        
        # 1. Convert Board tO ASP Facts
        facts_file = os.path.join(self.work_dir, "facts.txt")
        self._write_facts(pieces, turn_color_code, facts_file)
        print(f"[ASP AI] Fatti generati in: {facts_file}")

        # 2. Run DLV
        cmd = [self.dlv_path, self.rules_path, facts_file, "-n=1"] # Get 1 answer set
        print(f"[ASP AI] Esecuzione comando: {' '.join(cmd)}")
        
        try:
            # Capture output
            result = subprocess.run(cmd, capture_output=True, text=True)
            output = result.stdout
            print(f"[ASP AI] Output grezzo DLV:\n{output}")
            
            if result.stderr:
                print(f"[ASP AI] Errore DLV (stderr):\n{result.stderr}")

        except Exception as e:
            print(f"[ASP AI] Eccezione durante esecuzione DLV: {e}")
            return None

        # 3. Parse Output
        move = self._parse_output(output)
        if move:
            print(f"[ASP AI] Mossa interpretata: {move}")
        else:
            print("[ASP AI] Nessuna mossa trovata nell'output.")
            
        return move

    def _write_facts(self, pieces, turn_color_code, filename):
        with open(filename, "w") as f:
            # Map codes to ASP atoms
            # 1 = Black, 2 = White
            color_map = {0: "empty", 1: "black", 2: "white"}
            turn_atom = color_map.get(turn_color_code, "white") # Default safe
            
            f.write(f"turn({turn_atom}).\n")
            
            for r in range(5):
                for c in range(9):
                    val = pieces[r][c]
                    color = color_map.get(val, "empty")
                    # ASP uses cell(X,Y,Color). My grid is cell(Col, Row, Color)
                    f.write(f"cell({c},{r},{color}).\n")

    def _parse_output(self, output):
        # Allow extra output like "Best model:" etc.
        # Look for do_move(FX,FY,TX,TY,Type)
        # Regex to capture distinct patterns
        # Example: do_move(2,2,3,3,approach)
        match = re.search(r"do_move\((\d+),(\d+),(\d+),(\d+),([a-z]+)\)", output)
        if match:
            fx = int(match.group(1))
            fy = int(match.group(2))
            tx = int(match.group(3))
            ty = int(match.group(4))
            m_type = match.group(5)
            return (fx, fy, tx, ty, m_type)
        return None
