import json
import os
import csv
from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    """Kelas dasar untuk memuat, memproses, dan mengekspor data."""

    def __init__(self, input_path, json_key, output_path):
        self.input_path = input_path
        self.json_key = json_key
        self.output_path = output_path
        self.data = []

    def load_data(self, json_key=None):
        key = json_key or self.json_key
        with open(self.input_path, "r", encoding="utf-8") as file:
            content = json.load(file)

        if key not in content:
            raise KeyError(
                f'Key "{key}" tidak ditemukan dalam {self.input_path}. '
                f"Key yang tersedia: {list(content.keys())}"
            )

        self.data = content[key]
        print(f"Berhasil memuat {len(self.data)} data dari {self.input_path}")
        return self.data

    @abstractmethod
    def process_data(self):
        """Setiap kelas turunan harus mengimplementasikan proses_data."""
        raise NotImplementedError

    def export_to_csv(self, output_path=None):
        path = output_path or self.output_path
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

        if not self.data:
            print(f"Tidak ada data untuk diekspor ke {path}")
            return

        fieldnames = list(self.data[0].keys())
        with open(path, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(self.data)

        print(f"Berhasil mengekspor data ke {path}")
