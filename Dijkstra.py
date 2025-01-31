#This is the 2nd version !!!
#modifications in the branch1!
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fonction pour exécuter l'algorithme de Dijkstra
def calculate_dijkstra():
    source_node = "A"
    distances, predecessors = nx.single_source_dijkstra(G, source_node)

    # Nettoyer le tableau avant de l'afficher
    for row in tree.get_children():
        tree.delete(row)

    # Ajouter les résultats au tableau
    for node, distance in distances.items():
        path = nx.shortest_path(G, source=source_node, target=node, weight="weight")
        tree.insert("", "end", values=(node, distance, " -> ".join(path)))

# Créer la fenêtre principale
root = tk.Tk()
root.title("Algorithme de Dijkstra")
root.geometry("1200x700")
root.configure(bg="#2E3440")

# Styles modernes
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#3B4252", foreground="white", fieldbackground="#3B4252", rowheight=30, font=("Arial", 12))
style.configure("Treeview.Heading", background="#4C566A", foreground="white", font=("Arial Bold", 14))
style.configure("TButton", background="#88C0D0", foreground="#2E3440", font=("Arial Bold", 14))
style.map("TButton", background=[("active", "#5E81AC")])

# Zone pour le graphe
frame_graph = tk.Frame(root, bg="#2E3440")
frame_graph.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

# Zone pour les résultats
frame_results = tk.Frame(root, bg="#2E3440")
frame_results.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH)

# Ajouter un tableau pour afficher les résultats
tree = ttk.Treeview(frame_results, columns=("Sommet", "Distance", "Chemin"), show="headings", height=15)
tree.heading("Sommet", text="Sommet")
tree.heading("Distance", text="Distance")
tree.heading("Chemin", text="Chemin")
tree.column("Sommet", width=100, anchor="center")
tree.column("Distance", width=100, anchor="center")
tree.column("Chemin", width=500, anchor="w")
tree.pack(fill=tk.BOTH, expand=True, pady=10)

# Ajouter un bouton pour exécuter Dijkstra
calculate_button = ttk.Button(frame_results, text="Exécuter Dijkstra", command=calculate_dijkstra)
calculate_button.pack(pady=20)

# Créer le graphe
G = nx.DiGraph()  # Graphe orienté
edges = [
    ("E", "F", 5), ("F", "G", 10), ("G", "H", 14), ("G", "C", 1),
    ("H", "C", 9), ("E", "B", 4), ("A", "E", 8), ("A", "F", 2),
    ("D", "B", 6), ("A", "D", 5), ("B", "C", 6), ("D", "G", 1),
    ("D", "C", 4)
]
G.add_weighted_edges_from(edges)

# Dessiner le graphe avec matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(
    G, pos, with_labels=True, node_color="#5E81AC", node_size=2000,
    font_size=12, font_weight="bold", edge_color="#D8DEE9", ax=ax
)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)},
    font_color="#BF616A", ax=ax
)

# Intégrer la figure matplotlib dans Tkinter
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Titre principal
title_label = tk.Label(root, text="Algorithme de Dijkstra", bg="#2E3440", fg="#D8DEE9", font=("Arial Bold", 24))
title_label.pack(side=tk.TOP, pady=10)

# Lancer la boucle principale
root.mainloop()
