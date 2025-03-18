def bfs_find_answer(faq_graph, query):
    if query not in faq_graph:
        return "Pertanyaan tidak ditemukan dalam basis pengetahuan."

    from collections import deque  # Tambahkan impor ini

def bfs_find_answer(faq_graph, query):
    if query not in faq_graph:
        return "Pertanyaan tidak ditemukan dalam basis pengetahuan."
from collections import deque  # Tambahkan impor ini

def bfs_find_answer(faq_graph, query):
    if query not in faq_graph:
        return "Pertanyaan tidak ditemukan dalam basis pengetahuan."

    queue = deque([query])  # Mulai dari pertanyaan yang diberikan
    visited = set()

    while queue:
        node = queue.popleft()
        if node in faq_graph["answers"]:  # Jika node memiliki jawaban, kembalikan jawabannya
            return faq_graph["answers"][node]

        if node not in visited:
            visited.add(node)
            for neighbor in faq_graph.get(node, []):
                queue.append(neighbor)

    return "Tidak ada jawaban yang relevan ditemukan."



# Struktur grafik FAQ
faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks adalah model AI yang terinspirasi dari otak manusia.",
        "Supervised Learning": "Supervised Learning menggunakan data berlabel untuk pelatihan."
    }
}

# Contoh penggunaan
query = "What is AI?"
jawaban = bfs_find_answer(faq_graph, query)
print("Jawaban:", jawaban)