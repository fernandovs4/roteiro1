import socket
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# Função para escanear uma única porta
def scan_port(host, port, open_ports, well_known_ports, output_text, progress_bar, total_ports, current_progress):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            service = well_known_ports.get(port, "Unknown Service")
            open_ports.append((port, service))
            # Atualiza o texto na interface gráfica
            output_text.insert(tk.END, f"Port {port} open: {service}\n")
            output_text.yview(tk.END)  # Auto-scroll para o final

        # Atualiza a barra de progresso
        current_progress[0] += 1
        progress = (current_progress[0] / total_ports) * 100
        progress_bar['value'] = progress
        output_text.update_idletasks()

# Função para escanear portas com threads
def scan_ports_threaded(host, start_port, end_port, output_text, progress_bar):
    open_ports = []
    well_known_ports = {
        20: "FTP Data Transfer", 21: "FTP Control", 22: "SSH", 23: "Telnet",
        25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS"
    }
    
    total_ports = end_port - start_port + 1
    current_progress = [0]  # Usado para armazenar o progresso atual

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port, open_ports, well_known_ports, output_text, progress_bar, total_ports, current_progress))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        
    return open_ports

# Função para lidar com a execução da busca
def execute_scan():
    host = entry_host.get()
    try:
        start_port = int(entry_start_port.get())
        end_port = int(entry_end_port.get())
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        return
    
    # Limpa o texto antes de começar o novo escaneamento
    output_text.delete(1.0, tk.END)
    
    # Desabilita o botão durante o escaneamento
    btn_scan.config(state=tk.DISABLED)
    
    # Reseta a barra de progresso
    progress_bar['value'] = 0
    
    # Executa o escaneamento em uma thread separada
    def scan():
        open_ports = scan_ports_threaded(host, start_port, end_port, output_text, progress_bar)
        if not open_ports:
            output_text.insert(tk.END, "Nenhuma porta aberta encontrada.\n")
        else:
            output_text.insert(tk.END, "Scan completo.\n")
        output_text.yview(tk.END)  # Auto-scroll para o final
        btn_scan.config(state=tk.NORMAL)
    
    threading.Thread(target=scan).start()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Port Scanner")
root.geometry("600x450")

# Definindo as cores
bg_color = "#2c3e50"
fg_color = "#ecf0f1"
button_color = "#3498db"
entry_color = "#34495e"
highlight_color = "#e74c3c"

root.configure(bg=bg_color)

# Layout
tk.Label(root, text="Host:", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_host = tk.Entry(root, width=20, bg=entry_color, fg=fg_color, insertbackground=fg_color, relief=tk.FLAT)
entry_host.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Start Port:", bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_start_port = tk.Entry(root, width=20, bg=entry_color, fg=fg_color, insertbackground=fg_color, relief=tk.FLAT)
entry_start_port.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="End Port:", bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_end_port = tk.Entry(root, width=20, bg=entry_color, fg=fg_color, insertbackground=fg_color, relief=tk.FLAT)
entry_end_port.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

btn_scan = tk.Button(root, text="Scan", bg=button_color, fg=fg_color, activebackground=highlight_color, relief=tk.FLAT, command=execute_scan)
btn_scan.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Widget para exibir os resultados
output_text = tk.Text(root, height=15, width=60, bg=entry_color, fg=fg_color, relief=tk.FLAT)
output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
output_text.config(state=tk.NORMAL)  # Permite edição no widget de texto

# Barra de progresso
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Ajuste das colunas para expandir com o redimensionamento da janela
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
